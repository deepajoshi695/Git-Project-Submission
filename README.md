🕹️ Tic-Tac-Toe Git Mastery Project
A beginner-friendly Python Tic-Tac-Toe game developed to demonstrate Git workflow, branching strategies, and merge conflict resolution.
🚀 Features (The 5 Functions)
This project implements the following logic:
create_board(): Initializes a 3x3 grid with empty spaces.
display_board(): Renders the current state of the game in the console.
check_winner(): Evaluates the grid against 8 possible winning combinations.
is_board_full(): Determines if the game is a draw.
get_move(): Handles player input, validation, and error handling.
🛠️ Technical Workflow
1. Initialization & Configuration
Setup: Configured local Git identity using git config.
Initialization: Started the local repository with git init.
Main Branch: Created the base game.py with the board setup and pushed it to the GitHub remote repository.
2. Branching Strategy
I simulated a collaborative environment using three branches:
main: The stable production branch.
developer1: Used to implement the Win Logic.
developer2: Used to implement the Game Loop and Input Handling.
3. Meaningful Contribution & Conflict
To meet the project requirements, I deliberately created a Merge Conflict:
Dev1 updated the version tag to Version 1.1 (Dev1-Winner-Logic).
Dev2 updated the same line to Version 2.0 (Dev2-Final-Build).
4. Conflict Resolution
Successfully merged developer1 into main.
Triggered a conflict when merging developer2.
Resolution: Manually edited the file in VS Code, removing Git markers and keeping only the latest changes from developer2 to ensure the game was fully functional.
💻 How to Run
1. Clone the repository:
    bash
        git clone https://github.com
2. Navigate to the folder:
    bash
        cd Git-Project-Submission
3. Run the game:
    bash
        python game.py
🛠️Skills & Tools Used
    -Language: Python 3.x
    -IDE: VS Code
    -Version Control: Git & GitHub
    -Techniques: Branching, Merging, Conflict Resolution, Remote Tracking.



