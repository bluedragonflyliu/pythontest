import turtle
import math
t = turtle.Pen();

for i in range(1,6):
    t.forward(60)
    t.left(144)
t.color('red')
for i in range(1,5):
    if i==1:
        
        t.left(72)
        t.forward(30/math.cos(math.pi/5))
    t.right(72)   
    t.forward(30/math.cos(math.pi/5))


t.up();
t.goto(-200,-100)
t.down()
for x in range(1, 7):
    t.forward(30)
    t.left(120)
    t.forward(30)
    t.right(60)


    
