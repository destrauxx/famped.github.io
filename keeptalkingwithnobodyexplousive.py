from tkinter import *
# TODO change import method, to from tkinter import module


# Constants
CANVAS_SIZE = 600
FIGURE_SIZE = CANVAS_SIZE / 3
RATIO = CANVAS_SIZE // FIGURE_SIZE
BG_COLOR = 'black'
EMPTY = None

# Player setup
x = 'player 1'
o = 'player 2'
FIRST_PLAYER = X

class Board(Tk):
    def __init__(self, start_player):
        super().__init__()
    
    def build_grid(self, grid_color):
        pass

    def render_cross(self, posX, posY):
        pass

    def render_circle(self, posX, posY):
        pass

    def winner(self, player=None):
        pass



# Initialize game object and execute require methods
game_v1 = Board(start_player=FIRST_PLAYER)

# Run the game
game_v1.mainloop()

