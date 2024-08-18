const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const sqlite3 = require('sqlite3').verbose();
const app = express();

const db = new sqlite3.Database(':memory:');
let flag = process.env.FLAG
app.use(bodyParser.json());

db.serialize(() => {
    db.run("CREATE TABLE users (username TEXT, password TEXT)");
    db.run("INSERT INTO users (username, password) VALUES (?, ?)", ["admin", "password123"]);
    db.run("INSERT INTO users (username, password) VALUES (?, ?)", ["user", "password"]);
});

app.use(express.static(path.join(__dirname, 'public')));
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.post('/login', (req, res) => {
    const { username, password } = req.body;

    if (!username || !password) {
        return res.status(400).json({ error: "Username and password are required" });
    }

    const query = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;
    db.get(query, (err, row) => {
        if (err) {
            return res.status(500).send("Database error");
        }

        if (row) {
            if (username == "admin") {
                return res.send(`WELCOME ADMIN, HERE'S THE FLAG ${flag}`)
            } else {
                return res.send(`You logged in as ${username}...`)
            }
        } else {
            return res.status(401).send("Invalid credentials");
        }
    });
});
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});