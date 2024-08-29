const express = require("express");
const crypto = require("crypto");
const PORT = 8000;
const sha256 = (data) => crypto.createHash("sha256").update(data).digest("hex");
const app = express();
const session = require("express-session");
const MemoryStore = require("memorystore")(session)

app.use(express.static("public"));
app.use(express.json());

app.use(
    session({
        cookie: { maxAge: 3600000, httpOnly: false },
        store: new MemoryStore({
            checkPeriod: 3600000, // prune expired entries every 1h
        }),
        resave: false,
        saveUninitialized: false,
        secret: crypto.randomBytes(32).toString("hex"),
    })
);

const users = new Map();
const posts = new Array();

// Let me insert the flag into the db first :)
const admin_pass = crypto.randomBytes(8).toString("hex")
const flag = process.env.flag || "REP{FAKE_FLAG}"
users.set("admin", sha256(admin_pass));
posts.push({ user: "admin", title: "SECRET CONTENT", content: flag });


const is_invalid = (...args) => {
    return args.some(arg => !arg || typeof arg !== "string");
};
const make_error = (error) => ({ success: false, error })

app.post("/api/login", (req, res) => {
    let { user, pass } = req.body;
    if (is_invalid(user, pass)) {
        return res.json(make_error("Missing username or password"));
    }

    if (!users.has(user)) {
        return res.json(make_error("No user with that username exists"));
    }

    if (users.get(user) !== sha256(pass)) {
        return res.json(make_error("invalid password"));
    }
    req.session.user = user;
    res.json({ success: true });
});

app.post("/api/register", (req, res) => {
    let { user, pass } = req.body;
    if (is_invalid(user, pass)) {
        return res.json(make_error("Missing username or password"));
    }

    if (users.has(user)) {
        return res.json(make_error("A user exists with that username"));
    }

    req.session.user = user;
    users.set(user, sha256(pass));
    res.json({ success: true });
});

const auth = (req, res, next) =>
    req.session.user
        ? next()
        : res.json(make_error("You must be logged 2in!"));

app.post("/api/create", auth, (req, res) => {
    let { title, content } = req.body;
    if (is_invalid(title, content)) {
        return res.json(make_error("Missing title or content"))
    }
    posts.push({ user: req.session.user, title, content });
    res.json({ success: true });
});

app.post("/api/posts", auth, (req, res) => {
    return res.json({
        success: true,
        data: posts.filter(post => post.user === req.session.user)
    });
});

app.get("/api/search/:query", auth, (req, res) => {
    let { query } = req.params;
    if (!query) {
        return res.json(make_error("No query provided"))
    }
    const matching_posts = posts.filter(post => post.content.includes(query))
    if (matching_posts.length === 0) {
        return res.json({ success: false, results: [] })
    }
    const results = matching_posts.filter(post => post.user === req.session.user).map(post => ({ title: post.title, content: post.content }))
    return res.json({ success: true, results });
});



app.get("*", (req, res) => res.sendFile("index.html", { root: "public" }));
app.listen(PORT, () => console.log(`app listening on port ${PORT}`));
