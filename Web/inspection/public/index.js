var userScore = 0;
var CompScore = 0;
const userScore_span = document.getElementById("user-score");
const CompScore_span = document.getElementById("comp-score");
const ScoreBoard_div = document.querySelector(".score-board");
const Result_p = document.querySelector(".result > p");
const rock_div = document.getElementById("r");
const paper_div = document.getElementById("p");
const scissors_div = document.getElementById("s");
const smallUserWord = "user".fontsize(3).sub();
const smallCompWord = "comp".fontsize(3).sub();

function ConvertToWord(letter) {
    if (letter === "r") return "Rock";
    if (letter === "s") return "Scissors";
    return "Paper";
}

function getComputerChoice() {
    const choices = ['r', 'p', 's'];
    const randomNumber = Math.floor(Math.random() * 3)
    return choices[randomNumber];
}

function win(user, computer) {
    userScore++;
    userScore_span.innerHTML = userScore;
    CompScore_span.innerHTML = CompScore;
    // Most web vulnerabilities are due to javascript
    // Here's part3 of the flag: i5_r34d1ng_c0de
    Result_p.innerHTML = `${ConvertToWord(user)}${smallUserWord} beats ${ConvertToWord(computer)}${smallCompWord}. You win!`;
    document.getElementById(user).classList.add('green-glow');
    setTimeout(() => document.getElementById(user).classList.remove('green-glow'), 300);
}

function lose(user, computer) {
    CompScore++;
    userScore_span.innerHTML = userScore;
    CompScore_span.innerHTML = CompScore;
    Result_p.innerHTML = `${ConvertToWord(computer)}${smallCompWord} beats ${ConvertToWord(user)}${smallUserWord}. You lose!`;
    document.getElementById(user).classList.add('red-glow');
    setTimeout(() => document.getElementById(user).classList.remove('red-glow'), 300);
}

function draw(user, computer) {
    Result_p.innerHTML = `${ConvertToWord(computer)} equals ${ConvertToWord(user)}. It's a draw...`;
    document.getElementById(user).classList.add('grey-glow');
    setTimeout(() => document.getElementById(user).classList.remove('grey-glow'), 300);
}

function game(userChoice) {
    const ComputerChoice = getComputerChoice();
    switch (userChoice + ComputerChoice) {
        case "rs":
        case "sp":
        case "pr":
            win(userChoice, ComputerChoice);
            break;
        case "sr":
        case "ps":
        case "rp":
            lose(userChoice, ComputerChoice);
            break;
        case "ss":
        case "pp":
        case "rr":
            draw(userChoice, ComputerChoice);
            break;
    }
}

function main() {
    rock_div.addEventListener('click', () => game("r"));
    paper_div.addEventListener('click', () => game("p"));
    scissors_div.addEventListener('click', () => game("s"));
}



function run_this_function_to_get_the_flag_part3() {
    heehee = 'BYUwTiDkDOAEAOBDMAXWBmWB7AZrFosOANogOYBcsAxgCxjo4CuxxAngPpA='
    console.log(LZString.decompressFromBase64(heehee))
}


function decrypt() {
    let heeheehee = "9VWYmhjZxMjY2YWN5M2NiJmYlJmM3E2M1MWYhdDMhRmYg0DInFGbm9VZoR3Xm92X0JXYw9FdzFGb"
    let heeheeheehee = heeheehee.split('').reverse().join('');
    let heeheeheeheehee = atob(heeheeheehee)

    // Store the last part of the flag in a cookie
    // try reading it off your cookies
    document.cookie = `last_flag=${heeheeheeheehee}; path=/`;
}

main();
decrypt()