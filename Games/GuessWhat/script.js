const words = ["Candy", "Wonder", "Peculiar", "Horrendous", "Germinate", "Torrent", "Anaconda"];

function getWordOfTheDay() {
    const startDate = new Date('2023-01-01T00:01:00Z'); // Start date in UTC
    const now = new Date();
    const diffInDays = Math.floor((now - startDate) / (1000 * 60 * 60 * 24));
    return words[diffInDays % words.length];
}

let word = getWordOfTheDay().toLowerCase();
let currentLetterIndex = 1;
let guessCounter = 0;
let startTime;
let guessedWords = new Set();

document.getElementById('letter').innerText = word[0].toUpperCase();

function handleKeyPress(event) {
    if (event.key === 'Enter') {
        submitGuess();
    }
}

async function submitGuess() {
    const guessInput = document.getElementById('guess-input');
    const guess = guessInput.value.trim().toLowerCase();

    if (guessedWords.has(guess)) {
        shakeScreen();
        guessInput.value = '';
        return;
    }

    if (guess.startsWith(word.slice(0, currentLetterIndex))) {
        const isValidWord = await checkWordValidity(guess);
        if (!isValidWord) {
            shakeScreen();
            guessInput.value = '';
            return;
        }

        guessCounter++;
        updateGuessCounter();
        guessedWords.add(guess);

        const guessedList = document.getElementById('guessed-list');
        const listItem = document.createElement('li');
        listItem.innerText = guess;
        guessedList.appendChild(listItem);

        if (guess === word) {
            const endTime = new Date();
            const timeTaken = Math.floor((endTime - startTime) / 1000);
            document.getElementById('time-taken').innerText = timeTaken;
            document.getElementById('popup').classList.remove('hidden');
        } else if (guessCounter % 5 === 0) {
            currentLetterIndex++;
            document.getElementById('letter').innerText = word.slice(0, currentLetterIndex).toUpperCase();
            resetGuessCounter();
        }
    }

    guessInput.value = '';
}

async function checkWordValidity(word) {
    const response = await fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${word}`);
    return response.ok;
}

function updateGuessCounter() {
    const bubbles = document.querySelectorAll('.bubble');
    bubbles[(guessCounter - 1) % 5].classList.add('filled');
}

function resetGuessCounter() {
    const bubbles = document.querySelectorAll('.bubble');
    bubbles.forEach(bubble => bubble.classList.remove('filled'));
}

function shakeScreen() {
    const container = document.querySelector('.container');
    container.classList.add('shake');
    setTimeout(() => {
        container.classList.remove('shake');
    }, 500);
}

window.onload = function() {
    startTime = new Date();
}