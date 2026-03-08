markdown
# 🕹️ Tic-Tac-Toe: Git Mastery Project

A beginner-friendly Python game developed to demonstrate **Git Local Repository** management, **branching strategies**, and **conflict resolution**.

---

## 📂 Project Structure
```text
Git-Project-Submission/
├── .gitignore          # Excludes temporary Python files
├── README.md           # Project documentation (this file)
├── game.py             # Main Python script with 5 core functions
├── Demo.mp4            # Screen recording of project & Git workflow
└── Screenshots/        # Evidence of Git commands & outputs

🧠 Game Logic (The 5 Functions)
    1. create_board(): Initializes a 3x3 grid with empty spaces.
    2. display_board(): Renders the current state of the game board in the console.
    3. check_winner(): Evaluates the grid against 8 possible winning combinations.
    4. is_board_full(): Logic to determine if the game has ended in a draw.
    5. get_move(): Handles player input, ensures moves are within range (0-8), and validates if a spot is already taken.

🛠️ Git Implementation Workflow
    1. Initialization & Configuration
        - Configured local Git identity and initialized the repository using git init.
        - Created the base project structure and performed the First Commit on the main branch.

2. Branching & Contributions
    I simulated a collaborative development environment using three specific branches:
    - main: The stable source branch.
    - developer1: Implemented the Win Logic (Function 3).
    - developer2: Implemented the Game Loop (Functions 4 & 5).

3. Conflict Creation & Resolution
    To meet the project requirements, I deliberately triggered a Merge Conflict:
        - The Conflict: Both developer1 and developer2 modified the version/prompt line in the main logic at the same time.
        - The Resolution: I manually resolved the conflict in VS Code, choosing the latest functional code from developer2 to ensure a smooth gameplay experience.

🚀 How to Run the Project
    - Ensure you have Python 3.x installed.
    - Open your terminal and navigate to the project folder.
    - Run the following command:
        bash
        python game.py

🛠️ Skills & Techniques Used
    - Languages: Python
    - Tools: VS Code, Git, GitHub
    - Concepts: Git Tracking, Commits, Branching, Merging, Conflict Resolution, Remote Repositories.