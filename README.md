# 🎮 Tic-Tac-Toe: Git Submission Project

A terminal-based Tic-Tac-Toe game built with Python to demonstrate Git version control, branching strategies, and conflict resolution.

## 🚀 Features
- **Two-Player Gameplay:** Classic X and O turns.
- **5-Function Architecture:** Modular code design for readability.
    📝 Functions Breakdown
    The project implements the following 5 core functions:
    create_board(): Initializes the 3x3 grid.
    display_board(): Renders the current state of the game.
    check_winner(): Validates win conditions across rows, columns, and diagonals.
    is_board_full(): Checks for a draw state.
    get_move(): Handles and validates player input.

- **Robust Input Handling:** Prevents crashes from invalid or non-numeric moves.
- **Game State Logic:** Automatically detects wins and draws.

## 🛠️ Git & Branching Strategy
This project follows a specific branching model to simulate a collaborative environment:
- **main:** The stable production branch.
- **developer1:** Used for initial UI and welcome message updates.
- **developer2:** Used for custom game-start prompts.

### Conflict Resolution
A planned merge conflict was created by editing the same line in both developer branches. The conflict was resolved in the `main` branch by choosing the **latest changes** from `developer2`.

## 📂 Project Structure
- `game.py`: The main Python script containing the game logic.
- `.gitignore`: Configured to exclude `.venv` and Python cache files.
- `README.md`: Project documentation.

## ⚙️ How to Run
1. Ensure you have [uv](https://astral.sh) installed.
2. Clone the repository:
   ```bash
   git clone https://github.com
   cd Git-Project-Submission
Run the game:
bash
uv run game.py

