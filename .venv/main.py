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
    """Prints the game board from a dictionary."""
    print(f" {board['A1']} | {board['A2']} | {board['A3']} ")
    print("---|---|---")
    print(f" {board['B1']} | {board['B2']} | {board['B3']} ")
    print("---|---|---")
    print(f" {board['C1']} | {board['C2']} | {board['C3']} ")

board = """
    |    |       
____|____|____
    |    |     
____|____|____
    |    |    
    |    |    
"""

board_spots = """
 A1 | A2 | A3  
____|____|____
 B1 | B2 | B3  
____|____|____
 C1 | C2 | C3  
    |    |    
"""

def add_mark(position, letter):
    global board
    if position == "A1":
        modified_board = board[:3] + letter + board[4:]
    if position == "A2":
        modified_board = board[:8] + letter + board[9:]
    if position == "A3":
        modified_board = board[:13] + letter + board[14:]
    if position == "B1":
        modified_board = board[:36] + letter + board[37:]
    if position == "B2":
        modified_board = board[:41] + letter + board[42:]
    if position == "B3":
        modified_board = board[:46] + letter + board[47:]
    if position == "C1":
        modified_board = board[:67] + letter + board[68:]
    if position == "C2":
        modified_board = board[:72] + letter + board[73:]
    if position == "C3":
        modified_board = board[:77] + letter + board[78:]
    board = modified_board

def check_winner():
    if board[3] == board[8] == board[13] == "X" or board[36] == board[41] == board[46] == "X" or board[67] == board[72] == board[77] == "X" or board[3] == board[36] == board[67] == "X" or board[8] == board[41] == board[72] == "X" or board[13] == board[46]== board[77] == "X" or board[3] ==board[41]  == board[77] == "X" or board[13] == board[41] == board[67] == "X":
        print("X WINS! \n GAME OVER")
        return True
    elif board[3] == board[8] == board[13] == "O" or board[36] == board[41] == board[46] == "O" or board[67] == board[
        72] == board[77] == "O" or board[3] == board[36] == board[67] == "O" or board[8] == board[41] == board[
        72] == "O" or board[13] == board[46] == board[77] == "O" or board[3] == board[41] == board[77] == "O" or board[
        13] == board[41] == board[67] == "O":
        print("O WINS! \n GAME OVER")
        return True
    else:
        return False

game_over = False
print(logo)
print("Welcome to Tic Tac Toe!")
print(board_spots)
while not game_over:
    selected_square = input("Player 1, select your square: ")
    add_mark(selected_square, "X")
    print(board)
    if check_winner():
        break
    selected_square = input("Player 2, select your square: ")
    add_mark(selected_square, "O")
    print(board)
    check_winner()