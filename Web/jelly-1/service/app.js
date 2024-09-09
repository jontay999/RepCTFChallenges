const express = require('express');
const path = require('path');
const { CHALLENGE_LEVEL: level, Stage } = require("./server_jelly")

const app = express();
app.use(express.json());
app.enable('trust proxy')
app.use(express.static(path.join(__dirname, 'public')));
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

const FLAG = process.env.flag || "REP{FAKE_FLAG}"
const THE_TRUE_ADMIN = "<<<admin>>>"

// Start the server
const port = 3000;
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});

app.post('/validate', (req, res) => {
    console.log("===============================")
    console.log('Received a request to validate a user');
    let stage = new Stage(level);

    let moveHistory = req.body.moveHistory
    for (let i = 0; i < moveHistory.length; i++) {
        let move = moveHistory[i]
        let jelly = stage.jellies.find(j => j.x == move.x && j.y == move.y)
        stage.trySlide(jelly, move.dir)
    }
    // just in case XSS happens, I'll remove the <>'s
    let username = req.body.username.replace(/[<]/g, '%lt').replace(/[>]/g, '%gt');
    // but let me give you back 1 pair angle brackets
    let formatted_username = "<{username}>".replace("{username}", username)

    if (stage.checkForCompletion()) {
        if (req.ip === "localhost" && formatted_username === THE_TRUE_ADMIN) {
            res.send(`Congratulations ${formatted_username}! Here's the flag: ${FLAG}`)
        } else {
            res.send(`Congratulations ${formatted_username}! But I'll only give the flag to ${THE_TRUE_ADMIN} coming from localhost`)
        }
    } else {
        res.send("Incorrect solution!")
    }
});


