const express = require('express');
const path = require('path');
const { CHALLENGE_LEVEL: level, Stage } = require("./server_jelly")

const app = express();
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

const FLAG = process.env.flag || "REP{FAKE_FLAG}"

// Start the server
const port = 3000;
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});

app.post('/validate', (req, res) => {
    console.log("===============================")
    console.log('Received a request to validate a user');
    console.log(req.body)
    let stage = new Stage(level);

    let moveHistory = req.body

    console.log(stage.jellies)
    // console.log(stage)

    for (let i = 0; i < moveHistory.length; i++) {
        let move = moveHistory[i]
        let jelly = stage.jellies.find(j => j.x == move.x && j.y == move.y)
        stage.trySlide(jelly, move.dir)
    }

    if (stage.checkForCompletion()) {
        return res.json({
            message: "Level completed!",
            success: true,
            flag: FLAG
        })
    }

    return res.json({
        message: "Incorrect solution.",
        success: false
    })

});


