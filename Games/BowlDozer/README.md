# Endless Runner Game

## Overview
Endless Runner Game is a 2D game where the player controls a character running on a 2D plane. The objective is to collect points by hitting collectible items while avoiding obstacles.

## Assets
- **grey.png**: The character model used for the player.
- **pin.png**: The collectible item that the player can hit to gain points.
- **wall.png**: The obstacle that the player must jump over to avoid damage.

## Project Structure
```
endless-runner-game
├── assets
│   ├── grey.png
│   ├── pin.png
│   └── wall.png
├── src
│   ├── main.py
│   ├── game.py
│   ├── player.py
│   ├── obstacles.py
│   └── utils.py
├── requirements.txt
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd endless-runner-game
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Gameplay Mechanics
- The player controls a character that runs continuously.
- Collectibles (pins) can be hit to gain points.
- The player must jump over walls to avoid damage.

## How to Run
To start the game, run the following command:
```
python src/main.py
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.