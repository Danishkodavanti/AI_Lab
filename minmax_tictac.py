import math

# --- Tic Tac Toe board setup ---
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

# --- Minimax algorithm ---
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":  # AI wins
        return 1
    elif winner == "X":  # Human wins
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# --- Game loop ---
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("You are X, AI is O")
    print_board(board)

    while True:
        # Human turn
        x, y = map(int, input("Enter your move (row and column 0–2): ").split())
        if board[x][y] != " ":
            print("Invalid move! Try again.")
            continue
        board[x][y] = "X"
        print_board(board)

        if check_winner(board) == "X":
            print("🎉 You win!")
            break
        if is_full(board):
            print("🤝 It's a tie!")
            break

        # AI turn
        print("AI is making a move...")
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = "O"
        print_board(board)

        if check_winner(board) == "O":
            print("💀 AI wins!")
            break
        if is_full(board):
            print("🤝 It's a tie!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
