print('''
######### #########  #######  #########    ###     #######  #########  #######  #########
    #         #     #       #     #       #   #   #       #     #     #       # #
    #         #     #             #      #     #  #             #     #       # #
    #         #     #             #      #######  #             #     #       # #######
    #         #     #             #     #       # #             #     #       # #
    #         #     #       #     #     #       # #       #     #     #       # #
    #     #########  #######      #     #       #  #######      #      #######  ########
''')

spaces = {
    'A1': ' ', 'A2': ' ', 'A3': ' ',
    'B1': ' ', 'B2': ' ', 'B3': ' ',
    'C1': ' ', 'C2': ' ', 'C3': ' '
    }

def show_board():
    global board
    board = f'''
   1   2   3
A  {spaces['A1']} | {spaces['A2']} | {spaces['A3']}
  ------------
B  {spaces['B1']} | {spaces['B2']} | {spaces['B3']}
  ------------
C  {spaces['C1']} | {spaces['C2']} | {spaces['C3']}
'''
    print(board)

class Player:
    def __init__(self, x_o: str):
        self.x_o = x_o
        self.score = 0
        self.moves = []

    def play(self):
        global spaces
        while True:
            space = input("\nPlease type the name of a space to play: ").upper()
            if space in spaces.keys() and spaces[space] == " ":
                spaces[space] = self.x_o
                self.moves.append(space)
                if self.win(space):
                    show_board()
                    print("\nCONGRATULATIONS, YOU WIN!")
                    print(f"\nPlayer 1 Wins: {player1.score}\nPlayer 2 Wins: {player2.score}")
                    again = input("\nPlay again? ")
                    if again == "Y":
                        player1.moves = []
                        player2.moves = []
                        spaces = {
                            'A1': ' ', 'A2': ' ', 'A3': ' ',
                            'B1': ' ', 'B2': ' ', 'B3': ' ',
                            'C1': ' ', 'C2': ' ', 'C3': ' '
                            }
                        show_board()
                break
            else:
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
                if False not in filter(lambda x: x in self.moves, win_condition):
                    return True
        return False

def assign_player1():
    while True:
        x_o = input("\nPlease type 'X' or 'O' to start game. ").upper()
        if x_o == 'X' or x_o == 'O':
            return Player(x_o)
        print("\nNot a valid entry. Please try again.")

def assign_player2():
    if player1.x_o == 'X':
        return Player('O')
    return Player('X')

player1 = assign_player1()
player2 = assign_player2()
show_board()