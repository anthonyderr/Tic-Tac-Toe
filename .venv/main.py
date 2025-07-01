import os

logo=r"""
  _____ ___ ___         _____ _   ___         _____ ___  ___ 
 |_   _|_ _/ __|  ___  |_   _/_\ / __|  ___  |_   _/ _ \| __|
   | |  | | (__  |___|   | |/ _ \ (__  |___|   | || (_) | _| 
   |_| |___\___|         |_/_/ \_\___|         |_| \___/|___|                                                             """

# Clears the screen
def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def print_board(board):
    """Prints the game board from a list."""
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")




def update_board(position, letter):
    current_board[int(position)-1] = letter


# Winning combinations (indices)
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]  # Diagonals
]

board_map = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] # Creates a list for the board map
current_board = [" " for _ in range(9)] # Creates a list for the game board
player = 1
mark = "X"

def check_winner(board):
    # Check for winner
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != ' ':
            return board[combination[0]]
    # Check for Tie
    if " " not in board:
        return "TIE"

    return None # Game continues

def check_move(position):
    try:
        position = int(position)
        if 1 <= position <= 9 :
            if current_board[position-1] == " ":
                return True  # Returns True if the position is available
            else:
                print(f"Square {position} is already marked {current_board[position - 1]}.")
                return False
        else:
            print("Invalid Entry.  Please choose a square # (1-9).")
            return False
    except ValueError:
        print("Invalid Entry.  Please choose a square # (1-9).")
        return False






game_over = False

print(logo)
print("Welcome to Tic Tac Toe!")


while not game_over:
    print_board(board_map)
    position = input(f"Player {player} ({mark}), select a square: ")
    while not check_move(position):
        position = input(f"Player {player} ({mark}), select a square: ")
    #current_board[int(position)-1] = mark
    update_board(position, mark)
    print_board(current_board)
    print()
    winner = check_winner(current_board)
    if winner == "TIE":
        print("TIE!")
        break
    elif winner:
        print(f"Player {player} is the winner!")
        break

    # Switches between player 0 and player 1
    if player == 1:
        player = 2
        mark = "O"
    else:
        player = 1
        mark = "X"


print("Game Over.  Play again?")


