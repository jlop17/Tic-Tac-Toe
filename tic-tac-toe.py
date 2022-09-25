print('''
######### #########  #######  #########    ###     #######  #########  #######  #########
    #         #     #       #     #       #   #   #       #     #     #       # #
    #         #     #             #      #     #  #             #     #       # #
    #         #     #             #      #######  #             #     #       # #######
    #         #     #             #     #       # #             #     #       # #
    #         #     #       #     #     #       # #       #     #     #       # #
    #     #########  #######      #     #       #  #######      #      #######  ########
''')

grid = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

spaces = {
    'a1': grid[0][0], 'a2': grid[0][1], 'a3': grid[0][2],
    'b1': grid[1][0], 'b2': grid[1][1], 'b3': grid[1][2],
    'c1': grid[2][0], 'c2': grid[2][1], 'c3': grid[2][2]
    }

board = f'''
  {spaces['a1']} | {spaces['a2']} | {spaces['a3']} 
-------------
  {spaces['b1']} | {spaces['b2']} | {spaces['b3']} 
-------------
  {spaces['c1']} | {spaces['c2']} | {spaces['c3']} 
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
                break
            else:
                print("\nNot a valid space. Please try again.")
        print(board)

def assign_player():
    while True:
        x_o = input("\nPlease type 'X' or 'O' to start game")
        if x_o == 'X' or x_o == 'O':
            return Player(x_o)
        print("\nNot a valid entry. Please try again.")

while True:
    players = input("\n1 player or 2 players?")
    player1 = assign_player()
    if players == 1:
        break
    if players == 2:
        if player1.x_o == 'X':
            player2 = Player('O')
            break
        else:
            player2 = Player('X')
            break