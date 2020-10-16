from tkinter import *

root = Tk()


canvas = Canvas(root, width=600, height=600)
canvas.pack()

# canvas.create_line(0, 0, 600, 600)

# canvas.create_rectangle(10, 10, 50, 50, fill='greenyellow')


# canvas.create_rectangle(10, 10, 70, 70)
# canvas.create_rectangle(30, 30, 90, 90)
# canvas.create_line(10, 10, 30, 30)
# canvas.create_line(70, 10, 90, 30)
# canvas.create_line(10, 70, 30, 90)
# canvas.create_line(70, 70, 90, 90)

# canvas.create_oval(500, 500, 700, 700)
# canvas.create_text(200, 200, text='La casa de papel', fill='red', activefill='yellow', font='Arial 40')

# from time import sleep
# # circle_1 = canvas.create_oval(10, 10, 50, 50, fill='red')
# # circle_2 = canvas.create_oval(10, 10, 50, 50)


# # for i in range(100):
# #     canvas.move(circle_1, 1, 1)
# #     root.update()
# #     sleep(0.05)


# ghost = canvas.create_polygon(10, 10, 10, 60, 50, 35, fill='red')

# def move_triangle(event):
#     if event.keysym == 'Up':
#         canvas.move(ghost, 0, -3)
#     elif event.keysym == 'Down':
#         canvas.move(ghost, 0, 3)
#     elif event.keysym == 'Left':
#         canvas.move(ghost, -3, 0)
#     elif event.keysym == 'Right':
#         canvas.move(ghost, 3, 0)

# canvas.bind_all('<KeyPress>', move_triangle)

class Circle:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.size = 50
        self.speed_x = 3
        self.speed_y = 2
        self.canvas_size = 600
        self.object = canvas.create_oval(self.x, self.y, self.size, self.size, fill='yellow')

    def move(self):
        # self.x += self.speed_x
        # self.y += self.speed_y
        canvas.move(self.object, self.speed_x, self.speed_y)
        self.check_collision()
    
    def check_collision(self):
        pos = canvas.coords(self.object)
        if pos[0] <= 0:
            self.speed_x *= -1
        if pos[1] <= 0:
            self.speed_y *= -1
        if pos[2] >= self.canvas_size:
            self.speed_x *= -1
        if pos[3] >= self.canvas_size:
            self.speed_y *= -1


from time import sleep
c1 = Circle()

while True:
    c1.move()
    root.update()
    sleep(0.05)





























































root.mainloop()