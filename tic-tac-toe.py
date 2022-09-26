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

board = ''

def update_board():
    global board
    board = f'''
   1   2   3
A  {spaces['A1']} | {spaces['A2']} | {spaces['A3']}
  ------------
B  {spaces['B1']} | {spaces['B2']} | {spaces['B3']}
  ------------
C  {spaces['C1']} | {spaces['C2']} | {spaces['C3']}
'''

class Player:
    def __init__(self, x_o: str):
        self.x_o = x_o
        self.score = 0
        self.moves = []

    def play(self, space):
        while True:
            if space in spaces.keys() and spaces[space] == " ":
                spaces[space] = self.x_o
                self.moves.append(space)
                self.win(space)
                break
            else:
                print("\nNot a valid space. Please try again.")
        update_board()
        print(board)
    
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

def assign_player():
    while True:
        x_o = input("\nPlease type 'X' or 'O' to start game")
        if x_o == 'X' or x_o == 'O':
            return Player(x_o)
        print("\nNot a valid entry. Please try again.")

player1 = Player('X')
player1.play('A1')