let attempts;
let answer;
let maxAttempts = 10;

const inputs = [
    document.getElementById("number1"),
    document.getElementById("number2"),
    document.getElementById("number3")
];

const resultDiv = document.getElementById("results");
const submitButton = document.querySelector(".submit-button")
const resultImg = document.getElementById("game-result-img")
const attemptsSpan = document.getElementById("attempts");

function initGame() {
    attempts = maxAttempts;
    answer = generateAnswer();
    resultDiv.innerHTML = ''
    resultImg.src = ''
    attemptsSpan.textContent = attempts;
    inputs.forEach(input => input.value = "");
    submitButton.disabled = false;
}

function generateAnswer() {
    const nums = []
    while (nums.length < 3) {
        const rand = Math.floor(Math.random() * 10);
        if (!nums.includes(rand)) {
            nums.push(rand);
        }
    }
    return nums;
}

function check_numbers() {
    const userInput = inputs.map(input => input.value.trim());

    if (userInput.includes("")) {
        inputs.forEach(input => input.value = "");
        return;
    }

    const userNums = userInput.map(Number);

    const resultText = compareNumbers(userNums, answer);

    resultDiv.innerHTML += `<p>${userInput.join(", ")} → ${resultText}</p>`;

    attempts--;
    attemptsSpan.textContent = attempts;

    if (resultText === "3 스트라이크") {
        resultImg.src = "success.png";
        submitButton.disabled = true;
    } else if (attempts === 0) {
        resultImg.src = "fail.png";
        submitButton.disabled = true;
    }

    inputs.forEach(input => input.value = "");
}

function compareNumbers(userNums, answerNums) {
    let strike = 0;
    let ball = 0;

    for (let i = 0; i < 3; i++) {
        if (userNums[i] === answerNums[i]) strike++;
        else if (answerNums.includes(userNums[i])) ball++;
    }

    if (strike === 0 && ball === 0) return "O";
    return `${strike} S ${ball} B`;
}

window.onload = initGame;