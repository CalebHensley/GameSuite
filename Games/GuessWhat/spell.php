<?php
// spell.php
$words = ["example", "another", "wordlist"];
$selected_word = $words[array_rand($words)];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guess the Word Game</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Guess the Word Game</h1>
        <div id="game">
            <p id="first-letter">First Letter: <span id="letter"><?php echo $selected_word[0]; ?></span></p>
            <input type="text" id="guess-input" placeholder="Enter your guess">
            <button onclick="submitGuess()">Submit Guess</button>
            <p id="guess-counter">Guesses: <span id="counter">0</span></p>
            <div id="guessed-words">
                <h2>Guessed Words</h2>
                <ul id="guessed-list"></ul>
            </div>
        </div>
    </div>
    <div id="popup" class="hidden">
        <p>Congratulations! You guessed the word in <span id="time-taken"></span> seconds.</p>
        <button onclick="restartGame()">Play Again</button>
    </div>
    <script>
        let word = "<?php echo $selected_word; ?>";
        let currentLetterIndex = 1;
        let guessCounter = 0;
        let startTime;

        document.getElementById('letter').innerText = word[0];

        function submitGuess() {
            const guessInput = document.getElementById('guess-input');
            const guess = guessInput.value.trim().toLowerCase();
            
            if (guess.startsWith(word.slice(0, currentLetterIndex))) {
                guessCounter++;
                document.getElementById('counter').innerText = guessCounter;
                
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
                    document.getElementById('letter').innerText = word.slice(0, currentLetterIndex);
                }
            }
            
            guessInput.value = '';
        }

        function restartGame() {
            location.reload();
        }

        window.onload = function() {
            startTime = new Date();
        }
    </script>
</body>
</html>