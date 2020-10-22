from tkinter import *


#примечание для разработчиков - если в пункте TODO в конце написано "checked" пункт выполнен
root = Tk()
root.title('Godir 2')


canvas = Canvas(root, width=600, height=600, bg='ghost white')
canvas.pack()
root.resizable(0, 0)

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
# # canvas.move(circle_1, 1, 1)
# # root.update()
# # sleep(0.05)


# ghost = canvas.create_polygon(10, 10, 10, 60, 50, 35, fill='red')

# def move_triangle(event):
# if event.keysym == 'Up':
# canvas.move(ghost, 0, -3)
# elif event.keysym == 'Down':
# canvas.move(ghost, 0, 3)
# elif event.keysym == 'Left':
# canvas.move(ghost, -3, 0)
# elif event.keysym == 'Right':
# canvas.move(ghost, 3, 0)

# canvas.bind_all('<KeyPress>', move_triangle)

class Circle:
    '''
    Create a circle
    '''
    def __init__(self):
        self.x = 10
        self.y = 10
        self.size = 30
        self.speed_x = 5
        self.speed_y = 4
        self.canvas_size = 600
        self.object = canvas.create_oval(self.x, self.y, self.size, self.size, fill='LightSkyBlue2', outline='LightSkyBlue2')

    def move(self):
        '''
        result - a Circle have move
        '''
        # self.x += self.speed_x
        # self.y += self.speed_y
        canvas.move(self.object, self.speed_x, self.speed_y)
        self.check_collision()
        self.check_collision_with_platform()


    def check_collision(self):
        '''
        functional - check collision with walls
        '''
        #TODO: сделать проверку столкновения с платформой
        pos = canvas.coords(self.object)
        if pos[0] <= 0:
            self.speed_x *= -1
        if pos[1] <= 0:
            self.speed_y *= -1
        if pos[2] >= self.canvas_size:
            self.speed_x *= -1
        if pos[3] >= self.canvas_size:
            self.speed_y *= -1

    def check_collision_with_platform(self):
        #TODO сделать столкновения с боками
        pos_platform = p1.getter_coords()
        pos_circle = canvas.coords(self.object)

        if pos_circle[3] >= pos_platform[1] and pos_circle[2] >= pos_platform[0] and pos_circle[0] <= pos_platform[2] and pos_circle[1] <= pos_platform[3]:      #if circle have collision witn platform up - he is got around
            self.speed_y *= -1



class Platform():
    def __init__(self):
        self.x = 250
        self.y = 500
        self.size = 10
        self.canvas_size = 600
        self.object = canvas.create_rectangle(self.x, self.y, self.x + self.size*10, self.y + self.size, fill='yellow2', outline='yellow2')
        self.canvas = canvas
        self.canvas.bind_all('<KeyPress>', self.move)

    def move(self, event):
        if event.keysym == 'Left':
            canvas.move(self.object, -8, 0)
        elif event.keysym == 'Right':
            canvas.move(self.object, 8, 0)

        
        self.check_collision()
    

    def check_collision(self):
        #TODO: сделать проверку столкновения платформы со стеной (checked)
        posp = canvas.coords(self.object)            #pos = position, p = platform
        if posp[0] <= 0:
            canvas.move(self.object, 8, 0)
        elif posp[2] >= self.canvas_size:
            canvas.move(self.object, -8, 0)
    

    def getter_coords(self):
        posp = canvas.coords(self.object)
        return posp

from time import sleep
c1 = Circle()
p1 = Platform()
while True:
    c1.move()
    root.update()
    sleep(0.03)


























































root.mainloop()