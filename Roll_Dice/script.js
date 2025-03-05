let currentPlayer = 1;
let scores = { 1: { current: 0, saved: 0 }, 2: { current: 0, saved: 0 } };
const winningScore = 100;

// DOM Elements
const diceImage = document.getElementById("dice-image");
const rollDiceBtn = document.getElementById("roll-dice");
const saveScoreBtn = document.getElementById("save-score");
const resetGameBtn = document.getElementById("reset-game");
const winnerMessage = document.getElementById("winner-message");
const player1Section = document.getElementById("player1");
const player2Section = document.getElementById("player2");

//update to new scores
const updateScores = () => {
document.getElementById(`player1-current`).textContent = scores[1].current;
document.getElementById(`player1-saved`).textContent = scores[1].saved;
document.getElementById(`player2-current`).textContent = scores[2].current;
document.getElementById(`player2-saved`).textContent = scores[2].saved;
};




const switchPlayer = () => {
scores[currentPlayer].current = 0;
currentPlayer = currentPlayer === 1 ? 2 : 1;
updateScores();

//highlight the current playing player
player1Section.classList.toggle("active");
player2Section.classList.toggle("active");
};


rollDiceBtn.addEventListener("click", () => {
const diceRoll = Math.floor(Math.random() * 6) + 1;



diceImage.style.transform = "rotate(360deg)";
setTimeout(() => {
diceImage.src = `dice${diceRoll}.png`;
diceImage.style.transform = "rotate(0deg)";

  if (diceRoll === 1) {
    switchPlayer();
   } else {
       scores[currentPlayer].current += diceRoll;
       updateScores();
     }
    }, 300);
});



//save score to current score
saveScoreBtn.addEventListener("click", () => {
scores[currentPlayer].saved += scores[currentPlayer].current;
if (scores[currentPlayer].saved >= winningScore) {
winnerMessage.textContent = `${document.getElementById(`player${currentPlayer}-name`).value} Wins!! `;
winnerMessage.style.color = "green";
rollDiceBtn.disabled = true;
saveScoreBtn.disabled = true;
  return;
    }
    switchPlayer();
});

//resets game to new
resetGameBtn.addEventListener("click", () => {
scores = { 1: { current: 0, saved: 0 }, 2: { current: 0, saved: 0 } };
currentPlayer = 1;
winnerMessage.textContent = "";
rollDiceBtn.disabled = false;
saveScoreBtn.disabled = false;
updateScores();


player1Section.classList.add("active");
player2Section.classList.remove("active");
});