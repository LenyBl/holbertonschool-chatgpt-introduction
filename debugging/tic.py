#!/usr/bin/env python3

def print_board(board):
    """Prints the current state of the board."""
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)


def check_winner(board):
    """Checks if a player has won."""
    # Rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == 3:
            return True

    # Columns
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return True

    # Diagonals
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True

    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False


def board_full(board):
    """Checks if the board is full (draw condition)."""
    for row in board:
        if " " in row:
            return False
    return True


def get_valid_input(player):
    """Safely gets validated row and column input from the user."""
    while True:
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            if row not in range(3) or col not in range(3):
                print("❌ Coordinates must be 0, 1, or 2.")
                continue

            return row, col

        except ValueError:
            print("❌ Invalid input. Please enter numbers only.")


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        row, col = get_valid_input(player)

        if board[row][col] != " ":
            print("❌ That spot is already taken! Try again.")
            continue

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print(f"🎉 Player {player} wins!")
            break

        if board_full(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
