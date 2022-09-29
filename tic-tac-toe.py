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
    print(f"\nSCORE\n{player1.x_o}: {player1.score}\n{player2.x_o}: {player2.score}\nD: {draw_count}")
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
            move = input("\nType space to play: ").upper()
            if move in spaces.keys() and spaces[move] == " ":
                spaces[move] = self.x_o
                self.moves.append(move)
                if self.win(move):
                    display()
                    print(f"\n{self.x_o} WINS!")
                    rematch()
                if draw():
                    display()
                    print("\nDRAW!")
                    rematch()
                break
            if move == "QUIT":
                sys.exit()
            display()
            print("\nInvalid space. Please try again.")

    def win(self, move):
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
                count = 0
                for space in win_condition:
                    if space in self.moves:
                        count += 1
                    if count == 3:
                        self.score += 1
                        return True
        return False
    
def assign_players():
    while True:
        x_o = input("\n'X' or 'O'? ").upper()
        if x_o == 'X' or x_o == 'O':
            player1 = Player(x_o)
            break
        if x_o == "QUIT":
            sys.exit()
        title()
        print("\nInvalid entry. Please try again.")
    if player1.x_o == 'X':
        player2 = Player('O')
    else:
        player2 = Player('X')
    return player1, player2

draw_count = 0

def draw():
    global draw_count
    if ' ' not in spaces.values():
        draw_count += 1
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
            print("\n\nTHANKS FOR PLAYING!\n\n")
            sys.exit()
        display()
        print("Invalid entry. Please try again.")

title()
print("\n")

player1, player2 = assign_players()

current_player = player1
display()

while True:
    current_player = player1
    player1.play()
    current_player = player2
    player2.play()