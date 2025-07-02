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

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # Creates a list for the game board
        self.player = 1
        self.mark = "X"
        self.game_over = False

        # Winning combinations (indices)
        self.winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

    def print_game(self):
        """ Prints the game board from a list, prints the board map next to it"""
        print(" ========================================== ")
        print("||                                        ||")
        print("||                    |     1 | 2 | 3     ||")
        print(f"||     {self.board[0]} | {self.board[1]} | {self.board[2]}      |    ---|---|---    ||")
        print("||    ---|---|---     |     4 | 5 | 6     ||")
        print(f"||     {self.board[3]} | {self.board[4]} | {self.board[5]}      |    ---|---|---    ||")
        print("||    ---|---|---     |     7 | 8 | 9     ||")
        print(f"||     {self.board[6]} | {self.board[7]} | {self.board[8]}      |                   ||")
        print("||                    |     Board Map     ||")
        print("||                                        ||")
        print(" ========================================== ")

    def check_move(self, position):
        """Checks if the move is valid"""
        try:
            position = int(position)
            if 1 <= position <= 9 :
                if self.board[position-1] == " ":
                    return True  # Returns True if the position is available
                else:
                    print(f"Square {position} is already marked {self.board[position - 1]}.")
                    return False
            else:
                print("Invalid Entry.  Please choose a square # (1-9).")
                return False
        except ValueError:
            print("Invalid Entry.  Please choose a square # (1-9).")
            return False

    def update_board(self, position):
        """Adds a mark to the board"""
        self.board[int(position)-1] = self.mark

    def check_winner(self):
        """Checks for a winner or a tie"""
        # Check for winner
        for combination in self.winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != ' ':
                return self.board[combination[0]]
        # Check for Tie
        if " " not in self.board:
            return "TIE"

        return None # Game continues

    def switch_player(self):
        """Switches the current player"""
        if self.player == 1:
            self.player = 2
            self.mark = "O"
        else:
            self.player = 1
            self.mark = "X"

    def play(self):
        """Main game loop"""
        clear_screen()
        print(logo)
        print("Welcome to Tic Tac Toe!")
        print("Player 1 is X, Player 2 is O.  Players will alternate turns.")
        print()

        while not self.game_over:
            self.print_game()
            #Get player input
            position = input(f"Player {self.player} ({self.mark}), select a square (1-9) from the Board Map (1-9): ")
            while not self.check_move(position):
                position = input(f"Player {self.player} ({self.mark}), select a square from the Board Map (1-9): ")
            # current_board[int(position)-1] = mark
            self.update_board(position)
            self.print_game()
            print()
            winner = self.check_winner()
            if winner:
                clear_screen()
                print(logo)
                self.print_game()
                if winner == "TIE":
                    print("It's a TIE!  Good Game!")
                else:
                    print(f"Player {self.player} ({self.mark}) WINS!")
                self.game_over = True

            self.switch_player()

def main():
    """Main function to run the game"""
    while True:
        game = TicTacToe()
        game.play()
        play_again = input("Do you want to play again? (y/n): ").lower().strip()
        if play_again == "y":
            pass
        elif play_again == "n":
            print("Thanks for playing!")
            break
        else:
            print('Please enter "y" for yes or "n" for no')

if __name__ == "__main__":
    main()







