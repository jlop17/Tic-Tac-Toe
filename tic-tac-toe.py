import sys
import os

spaces = {
    'A1': ' ', 'A2': ' ', 'A3': ' ',
    'B1': ' ', 'B2': ' ', 'B3': ' ',
    'C1': ' ', 'C2': ' ', 'C3': ' '
    }

draws = 0

def title():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
XXXXXXXXX OOOOOOOOO  XXXXXXX  OOOOOOOOO    XXX     OOOOOOO  XXXXXXXXX  OOOOOOO  XXXXXXXX
    X         O     X       X     O       X   X   O       O     X     O       O X
    X         O     X             O      X     X  O             X     O       O X
    X         O     X             O      XXXXXXX  O             X     O       O XXXXXXX
    X         O     X             O     X       X O             X     O       O X
    X         O     X       X     O     X       X O       O     X     O       O X
    X     OOOOOOOOO  XXXXXXX      O     X       X  OOOOOOO      X      OOOOOOO  XXXXXXXX
''')

def display():
    global board
    board = f'''
   1   2   3
A  {spaces['A1']} | {spaces['A2']} | {spaces['A3']}
  ------------
B  {spaces['B1']} | {spaces['B2']} | {spaces['B3']}
  ------------
C  {spaces['C1']} | {spaces['C2']} | {spaces['C3']}
'''
    title()
    print(f"\nSCORE\n{player1.x_o}: {player1.score}\n{player2.x_o}: {player2.score}\nD: {draws}")
    print(board)

def quit():
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.exit()

class Player:
    def __init__(self, x_o: str):
        self.x_o = x_o
        self.score = 0
        self.owned_spaces = []

    def turn(self):
        def win(move):
            win_conditions = [
                ('A1', 'A2', 'A3'),
                ('B1', 'B2', 'B3'),
                ('C1', 'C2', 'C3'),
                ('A1', 'B1', 'C1'),
                ('A2', 'B2', 'C2'),
                ('A3', 'B3', 'C3'),
                ('A1', 'B2', 'C3'),
                ('C1', 'B2', 'A3')
            ]

            for win_condition in win_conditions:
                if move in win_condition:
                    count = 1
                    checklist = [space for space in win_condition if space != move]
                    for space in checklist:
                        if space not in self.owned_spaces:
                            break
                        count += 1
                        if count == 3:
                            self.score += 1
                            return True
            return False

        def rematch():
            global spaces
            while True:
                rematch = input("\nPlay again (Y/N)? ").upper()
                if rematch == "Y":
                    player1.owned_spaces = []
                    player2.owned_spaces = []
                    spaces = {
                        'A1': ' ', 'A2': ' ', 'A3': ' ',
                        'B1': ' ', 'B2': ' ', 'B3': ' ',
                        'C1': ' ', 'C2': ' ', 'C3': ' '
                        }
                    break
                if rematch == "N" or rematch == "QUIT" or rematch == "EXIT":
                    quit()
                display()
                print("\nInvalid entry. Please try again.")

        def mark(move):
            global draws
            spaces[move] = self.x_o
            self.owned_spaces.append(move)
            if win(move):
                display()
                print(f"\n{self.x_o} WINS!")
                rematch()
            elif ' ' not in spaces.values():
                draws += 1
                display()
                print("\nDRAW!")
                rematch()

        def play():
            display()
            print(f"\n{self.x_o} Turn")
            while True:
                move = input("\nType SPACE NAME to PLAY: ").upper()
                try:
                    if isinstance(int(move[0]), int):
                        move = move[1] + move[0]
                except ValueError:
                    pass
                finally:
                    if move in spaces.keys() and spaces[move] == " ":
                        mark(move)
                        break
                    if move == "QUIT" or move == "EXIT":
                        quit()
                display()
                print(f"\n{self.x_o} Turn")
                print("\nInvalid entry. Please try again.")

        def autoplay():
            for move, mark in spaces.items():
                if mark == ' ':
                    mark(move)

        if list(spaces.values()).count(' ') == 1:
            autoplay()
        else:
            play()

title()
print("\n")

while True:
    x_o = input("\n'X' or 'O'? ").upper()
    if x_o == 'X' or x_o == 'O':
        player1 = Player(x_o)
        break
    if x_o == "QUIT" or x_o == "EXIT":
        quit()
    title()
    print("\nInvalid entry. Please try again.")
if player1.x_o == 'X':
    player2 = Player('O')
else:
    player2 = Player('X')

while True:
    player1.turn()
    player2.turn()