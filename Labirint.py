from tkinter import *
from random import randint
# Constants
CANVAS_SIZE = 600
RECT_SIZE = CANVAS_SIZE // 20
RATIO = CANVAS_SIZE // RECT_SIZE
BG_COLOR = 'black'
PLAYER_X = CANVAS_SIZE // 2 - RECT_SIZE
PLAYER_Y = CANVAS_SIZE // 2 - RECT_SIZE
EMPTY = None

class Board(Tk):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas(width=CANVAS_SIZE, height=CANVAS_SIZE)
        self.canvas.pack()
        self.rect_size = RECT_SIZE
        self.player_x = PLAYER_X
        self.player_y = PLAYER_Y
        self.ratio = RATIO
        self.empty = EMPTY
        # self.canvas.bind_all('<KeyPress>', player_move)

    def build_grid(self):
        row = [self.empty] * self.rect_size
        col = []
        for _ in range(self.rect_size): 
            col.append(row[:])
        return col

    def render_obstacles(self):
        '''Magic number: 3, its a gap between edges and figure
        '''
        field = self.build_grid()
        x1 = 3
        y1 = 3
        x2 = self.rect_size - 3
        y2 = self.rect_size - 3
        chance = 30
        for r in range(self.ratio):
            for c in range(self.ratio):
                if field[r][c] == None:
                    r_num = randint(0, 100)
                    if r_num <= chance:
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill='black')
                y1 += self.rect_size
                y2 += self.rect_size
            y1 = 3
            y2 = self.rect_size - 3
            x1 += self.rect_size
            x2 += self.rect_size
        return field

    def render_player(self):
        '''Magic number: 3, its a gap between edges and figure
        Render player on field
        '''
        r_size = self.rect_size - 3
        player = self.canvas.create_oval(self.player_x, self.player_y, self.player_x + r_size, self.player_y + r_size, fill='red')


    def player_move(self):
        pass

board = Board()



# Test (finished)
board.render_obstacles()

board.mainloop()