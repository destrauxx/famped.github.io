import turtle
import random

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
        t.speed(100)
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
    
class Trtl():
    def __init__(self, color, start):
        self.color = color
        self.start = start
        self.turt = turtle.Turtle()
    
    def create(self):
        
        self.turt.penup()
        self.turt.shape('turtle')
        self.turt.fillcolor(self.color)
        self.turt.goto(self.start[0], self.start[1])

    def walk(self, step):
        self.turt.forward(step)
    
    def check_finish():
        

step = random.randint(1, 5)

road = Road(size_f)
start = [-310, 80]   
end = [-310 - size_f]      
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

while True:
    yellow.walk(step)
    red.walk(step)
    lime.walk(step)
    blue.walk(step)


screen.mainloop()

