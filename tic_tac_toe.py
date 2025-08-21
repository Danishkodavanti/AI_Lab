import random

# Constants to represent the players
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

# Function to print the game board
def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("---------")
    print()

# Function to check if a player has won
def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to check if the board is full (draw)
def is_board_full(board):
    return all(spot != EMPTY for spot in board)

# Minimax algorithm to calculate the best move for the AI
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, PLAYER_X):
        return -10 + depth
    if check_winner(board, PLAYER_O):
        return 10 - depth
    if is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_O
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = EMPTY
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_X
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = EMPTY
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Function to get the best move for the AI
def get_best_move(board):
    best_move = None
    best_value = float('-inf')

    for i in range(9):
        if board[i] == EMPTY:
            board[i] = PLAYER_O
            move_value = minimax(board, 0, False, float('-inf'), float('inf'))
            board[i] = EMPTY
            if move_value > best_value:
                best_value = move_value
                best_move = i
    return best_move

# Function to play the game
def play_game():
    board = [EMPTY] * 9
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        # Player's move (X)
        player_move = int(input("Enter your move (0-8): "))
        if board[player_move] == EMPTY:
            board[player_move] = PLAYER_X
        else:
            print("Invalid move, try again.")
            continue
        
        if check_winner(board, PLAYER_X):
            print_board(board)
            print("You win!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # AI's move (O)
        ai_move = get_best_move(board)
        board[ai_move] = PLAYER_O
        print(f"AI chose position {ai_move}")
        
        if check_winner(board, PLAYER_O):
            print_board(board)
            print("AI wins!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        print_board(board)

# Run the game
if __name__ == "__main__":
    play_game()
