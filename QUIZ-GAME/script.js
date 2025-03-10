const startScreen = document.getElementById("start-screen");
const quizScreen = document.getElementById("quiz-screen");
const endScreen = document.getElementById("end-screen");

const categorySelect = document.getElementById("category");
const difficultySelect = document.getElementById("difficulty");
const startBtn = document.getElementById("start-btn");
const restartBtn = document.getElementById("restart-btn");

const questionText = document.getElementById("question-text");
const optionsContainer = document.getElementById("options-container");
const timerText = document.getElementById("time-left");
const scoreText = document.getElementById("score");

let questions = [];
let currentQuestionIndex = 0;
let score = 0;
let timer;
let timeLeft = 15;
let optionSelected = false;

// Correct category mappings with valid OpenTDB IDs
const categoryMap = {
    "General Knowledge": 9,
    "Science & Nature": 17,
    "Computers": 18,
    "Geography": 22,
    "History": 23
};


function decodeHTMLEntities(text) {
    let textarea = document.createElement("textarea");
    textarea.innerHTML = text;
    return textarea.value;
}

// Fetch questions from API
async function fetchQuestions() {
    const category = categorySelect.value;
    const difficulty = difficultySelect.value;
    const categoryID = categoryMap[category];
    const apiUrl = `https://opentdb.com/api.php?amount=15&category=${categoryID}&type=multiple&difficulty=${difficulty}`;
    
    try {
        const response = await fetch(apiUrl);
        const data = await response.json();
        if (data.response_code !== 0) {
            alert("No questions available for this category. Please try another.");
            return;
        }
        questions = data.results;
        startGame();
    } catch (error) {
        console.error("Error fetching questions:", error);
    }
}


function startGame() {
    startScreen.classList.add("hidden");
    quizScreen.classList.remove("hidden");
    currentQuestionIndex = 0;
    score = 0;
    showQuestion();
}


function showQuestion() {
    if (currentQuestionIndex >= questions.length) {
        endGame();
        return;
    }

    optionSelected = false;
    const currentQuestion = questions[currentQuestionIndex];
    questionText.innerHTML = `<b>Q${currentQuestionIndex + 1}:</b> ${decodeHTMLEntities(currentQuestion.question)}`;

    optionsContainer.innerHTML = "";
    let answers = [...currentQuestion.incorrect_answers, currentQuestion.correct_answer];
    answers.sort(() => Math.random() - 0.5);

    answers.forEach(answer => {
        const btn = document.createElement("button");
        btn.innerText = decodeHTMLEntities(answer);
        btn.classList.add("option-btn");
        btn.onclick = () => selectAnswer(btn, answer, currentQuestion.correct_answer);
        optionsContainer.appendChild(btn);
    });

    timeLeft = 15;
    timerText.innerText = timeLeft;
    startTimer();
}


function startTimer() {
    clearInterval(timer);
    timer = setInterval(() => {
        timeLeft--;
        timerText.innerText = timeLeft;
        if (timeLeft <= 0) {
            clearInterval(timer);
            showCorrectAnswer();
        }
    }, 1000);
}

// Prevent multiple option selection and highlight correct/incorrect answers
function selectAnswer(button, selectedAnswer, correctAnswer) {
    if (optionSelected) return;
    optionSelected = true;

    clearInterval(timer);
    let buttons = document.querySelectorAll(".option-btn");

    buttons.forEach(btn => {
        if (btn.innerText === decodeHTMLEntities(correctAnswer)) {
            btn.classList.add("correct-answer");
        }
        if (btn === button && selectedAnswer !== decodeHTMLEntities(correctAnswer)) {
            btn.classList.add("wrong-answer");
        }
        btn.disabled = true;
    });

    if (selectedAnswer === decodeHTMLEntities(correctAnswer)) {
        score++;
    }

    setTimeout(() => {
        currentQuestionIndex++;
        showQuestion();
    }, 1500);
}

// show correct answer when time runs out
function showCorrectAnswer() {
    let buttons = document.querySelectorAll(".option-btn");

    buttons.forEach(btn => {
        if (btn.innerText === decodeHTMLEntities(questions[currentQuestionIndex].correct_answer)) {
            btn.classList.add("correct-answer");
        }
        btn.disabled = true;
    });

    setTimeout(() => {
        currentQuestionIndex++;
        showQuestion();
    }, 1500);
}


function endGame() {
    quizScreen.classList.add("hidden");
    endScreen.classList.remove("hidden");
    scoreText.innerText = `${score} / ${questions.length}`;
}


restartBtn.addEventListener("click", () => {
    endScreen.classList.add("hidden");
    startScreen.classList.remove("hidden");
});


startBtn.addEventListener("click", fetchQuestions);
