from collections import namedtuple

print('''
######### #########  #######  #########    ###     #######  #########  #######  #########
    #         #     #       #     #       #   #   #       #     #     #       # #
    #         #     #             #      #     #  #             #     #       # #
    #         #     #             #      #######  #             #     #       # #######
    #         #     #             #     #       # #             #     #       # #
    #         #     #       #     #     #       # #       #     #     #       # #
    #     #########  #######      #     #       #  #######      #      #######  #########
''')

grid = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

coords = ((0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2))

space = namedtuple("space", "grid, coords")

A1 = space(grid[0][0], coords[0])
A2 = space(grid[0][1], coords[1])
A3 = space(grid[0][2], coords[2])
B1 = space(grid[1][0], coords[3])
B2 = space(grid[1][1], coords[4])
B3 = space(grid[1][2], coords[5])
C1 = space(grid[2][0], coords[6])
C2 = space(grid[2][1], coords[7])
C3 = space(grid[2][2], coords[8])

spaces = {
    'A1': [A1.grid, A1.coords], 'A2': [grid[0][1], coords[1]], 'A3': [grid[0][2], coords[2]],
    'B1': [grid[1][0], coords[3]], 'B2': [grid[1][1], coords[4]], 'B3': [grid[1][2], coords[5]],
    'C1': [grid[2][0], coords[6]], 'C2': [grid[2][1], coords[7]], 'C3': [grid[2][2], coords[8]]
    }

board = f'''
   1   2   3
A  {spaces['A1'][0]} | {spaces['A2'][0]} | {spaces['A3'][0]}
  ------------
B  {spaces['B1'][0]} | {spaces['B2'][0]} | {spaces['B3'][0]}
  ------------
C  {spaces['C1'][0]} | {spaces['C2'][0]} | {spaces['C3'][0]}
'''

class Player:
    def __init__(self, x_o: str):
        self.x_o = x_o
        self.score = 0
        self.moves = []

    def play(self, space):
        while True:
            if space in spaces.keys() and spaces[space][0] == " ":
                grid = self.x_o
                self.moves.append(space)
                win_check(space)
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

def win_check(space):
    move_coord = spaces[spaces][1]
    directions = ((move_coord))
    pass

print(board)