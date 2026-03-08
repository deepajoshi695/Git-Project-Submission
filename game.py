# Function 1: Initializing the board
def create_board():
    return [' ' for _ in range(9)]

# Function 2: Board dispaly
def display_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

# Function 3: Checking for winner
def check_winner(board):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    return None

# Function 4: Checking if board is full (The 4th Function)
def is_board_full(board):
    return ' ' not in board

# Function 5: Handling player move logic (The 5th Function)
def get_move(player, board):
    try:
        move = int(input(f"Player {player}, enter position (0-8): "))
        if 0 <= move <= 8 and board[move] == ' ':
            return move
        print("Position already taken, choose different position.")
        return None
    except ValueError:
        print("Enter a number!")
        return None

# --- Main Logic
if __name__ == "__main__":
    while True:  # -- Play again loop
        board = create_board()
        current_player = "X"
        game_active = True
        
        print("--- Dev1 Version ---")

        while game_active:
            display_board(board)
            move = get_move(current_player, board)
            
            if move is not None:
                board[move] = current_player
                
                # Checking for win or draw
                winner = check_winner(board)
                if winner:
                    display_board(board)
                    print(f"🎉 Player {winner} wins!")
                    game_active = False
                elif is_board_full(board):
                    display_board(board)
                    print("🤝 It's a draw!")
                    game_active = False
                else:
                    # Switching players
                    current_player = "O" if current_player == "X" else "X"

        # The "Play Again" Prompt
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for playing! Goodbye.")
            break

