import sys
import os

spaces = {
    'A1': ' ', 'A2': ' ', 'A3': ' ',
    'B1': ' ', 'B2': ' ', 'B3': ' ',
    'C1': ' ', 'C2': ' ', 'C3': ' '
    }

def title():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
######### #########  #######  #########    ###     #######  #########  #######  #########
    #         #     #       #     #       #   #   #       #     #     #       # #
    #         #     #             #      #     #  #             #     #       # #
    #         #     #             #      #######  #             #     #       # #######
    #         #     #             #     #       # #             #     #       # #
    #         #     #       #     #     #       # #       #     #     #       # #
    #     #########  #######      #     #       #  #######      #      #######  ########
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
    print(f"\nScore\n{player1.x_o}: {player1.score}\n{player2.x_o}: {player2.score}")
    print(board)
    print(f"\n{current_player.x_o} Turn")

class Player:
    def __init__(self, x_o: str):
        self.x_o = x_o
        self.score = 0
        self.moves = []

    def play(self):
        global spaces
        display()
        while True:
            space = input("\nPlease type the name of a space to play: ").upper()
            if space in spaces.keys() and spaces[space] == " ":
                spaces[space] = self.x_o
                self.moves.append(space)
                if self.win(space):
                    self.score += 1
                    display()
                    print(f"\n{self.x_o} WINS!")
                    rematch()
                if draw():
                    display()
                    print("\nDRAW!")
                    rematch()
                break
            if space == "EXIT":
                sys.exit()
            display()
            print("\nNot a valid space. Please try again.")

    def win(self, space):
        win_conditions = [
            [space for space in spaces if space[0] == 'A'],
            [space for space in spaces if space[0] == 'B'],
            [space for space in spaces if space[0] == 'C'],
            [space for space in spaces if space[1] == '1'],
            [space for space in spaces if space[1] == '2'],
            [space for space in spaces if space[1] == '3'],
            ['A1', 'B2', 'C3'],
            ['C1', 'B2', 'A3']
        ]

        for win_condition in win_conditions:
            if space in win_condition:
                count = 0
                for space in win_condition:
                    if space in self.moves:
                        count += 1
                    if count == 3:
                        return True
        return False
    
def assign_player1():
    title()
    print("\n")
    while True:
        x_o = input("\nPlease type 'X' or 'O' to start game. ").upper()
        if x_o == 'X' or x_o == 'O':
            return Player(x_o)
        if x_o == "EXIT":
            sys.exit()
        title()
        print("\nNot a valid entry. Please try again.")

def assign_player2():
    if player1.x_o == 'X':
        return Player('O')
    return Player('X')

def draw():
    if ' ' not in spaces.values():
        return True
    return False

def rematch():
    global spaces
    while True:
        rematch = input("\nPlay again (Y/N)? ").upper()
        if rematch == "Y":
            player1.moves = []
            player2.moves = []
            spaces = {
                'A1': ' ', 'A2': ' ', 'A3': ' ',
                'B1': ' ', 'B2': ' ', 'B3': ' ',
                'C1': ' ', 'C2': ' ', 'C3': ' '
                }
            display()
            break
        if rematch == "N":
            print("\nTHANKS FOR PLAYING!")
            sys.exit()
        display()
        print("Not a valid entry. Please try again.")

player1 = assign_player1()
player2 = assign_player2()

current_player = player1

display()

while True:
    current_player = player1
    player1.play()
    current_player = player2
    player2.play()