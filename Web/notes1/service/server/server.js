const express = require("express");
const crypto = require("crypto");
const PORT = process.env.PORT || 8080;
const sha256 = (data) => crypto.createHash("sha256").update(data).digest("hex");

const app = express();
const session = require("express-session");
const MemoryStore = require("memorystore")(session)

app.use(
    session({
        cookie: { maxAge: 3600000 },
        store: new MemoryStore({
            checkPeriod: 3600000, // prune expired entries every 1h
        }),
        resave: false,
        saveUninitialized: false,
        secret: crypto.randomBytes(32).toString("hex"),
    })
);
app.use(express.json());

const users = new Map();
const posts = new Map();
const is_invalid = (...args) => {
    return args.some(arg => !arg || typeof arg !== "string");
};
const make_error = (error) => { success: false, error }

// Might need to adjust the content-security-policy
app.use((req, res, next) => {
    res.setHeader(
        "Content-Security-Policy",
        "script-src 'self'; object-src 'none'; base-uri 'none';"
    );
    if (req.session.user && users.has(req.session.user)) {
        req.user = users.get(req.session.user);
    }
    next();
});

app.post("/api/login", (req, res) => {
    let { user, pass } = req.body;
    if (is_invalid(user, pass)) {
        return res.json(make_error("Missing username or password"));
    }

    if (!users.has(user)) {
        return res.json(make_error("No user with that username exists"));
    }

    if (users.get(user).pass !== sha256(pass)) {
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
    users.set(user, { pass: sha256(pass), posts: [] });
    res.json({ success: true });
});

const auth = (req, res, next) =>
    req.user
        ? next()
        : res.json(make_error("You must be logged in!"));

app.post("/api/create", auth, (req, res) => {
    if (req.session.user === "admin") {
        return res.json(make_error("You are not admin..."))
    }

    let { title, body } = req.body;
    if (is_invalid(title, body)) {
        return res.json(make_error("Missing title or body"))
    }

    let id = crypto.randomBytes(6).toString("hex");
    posts.set(id, { id, title, body });
    req.user.posts.push(id);
    res.json({ success: true });
});

app.post("/api/posts", auth, (req, res) => {
    return res.json({
        success: true,
        data: req.user.posts.map((id) => posts.get(id)),
    });
});

app.get("/api/post/:id", auth, (req, res) => {
    let { id } = req.params;
    if (!id) {
        return res.json(make_error("No id provided"))
    }
    if (!posts.has(id)) {
        return res.json(make_error("No post with that id"))
    }
    return res.json({ success: true, data: posts.get(id) });
});

app.listen(PORT, () => console.log(`app listening on port ${PORT}`));
