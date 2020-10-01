import turtle
import random
from turtle import Turtle

screen = turtle.getscreen()
t = turtle.Turtle()

window = turtle.Screen()
window.bgcolor('green')

# t.shape('turtle')

size_f = int(input('Введи размер поля(100 макс.): '))

class Road():
    def __init__(self, size):
        self.size = size
    
    def build(self, size):
        spawn = [-300, 100]
        t.penup()
        t.goto(spawn[0], spawn[1])
        t.right(90)
        for i in range(int(self.size / 10)):
            for j in range(10):
                t.fd(5)
                t.penup()
                t.fd(5)
                t.pendown()
            t.penup()
            spawn[0] = spawn[0] + 20
            t.goto(spawn[0], spawn[1])
    
class Trtl(Turtle):
    def __init__(self, color, start):
        super().__init__()
        self.color = color
        self.start = start
    
    def create(self):
        self.penup()
        self.pencolor(self.color)
        self.shape('turtle')
        self.fillcolor(self.color)
        self.goto(self.start[0], self.start[1])

    def walk(self, step):
        self.pendown()
        self.forward(step)
    
    def check_finish(self, status):
        print(self.xcor())
        if self.xcor() == end:
            self.penup()
            self.hideturtle()
            

step = random.randint(1, 2)

road = Road(size_f)
start = [-310, 80]   
end = -310 + size_f * 2      
road.build(size_f) 



yellow = Trtl('yellow', start)
yellow.create()

start[1] -= 20

red = Trtl('red', start)
red.create()

start[1] -= 20

lime = Trtl('lime', start)
lime.create()

start[1] -= 20


blue = Trtl('blue', start)
blue.create()

start[1] -= 20

status = True
while status:

    yellow.check_finish(status)
    red.check_finish(status)
    lime.check_finish(status)
    blue.check_finish(status)

    yellow.walk(step)
    red.walk(step)
    lime.walk(step)
    blue.walk(step)



screen.mainloop()