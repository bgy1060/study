import random
import turtle as t

t.shape('turtle')
t.speed('fastest')
t.bgcolor('black')
for i in range(300):
    if i%4==0:
        t.color("red")
    elif i%4==1:
        t.color("green")
    elif i%4==2:
        t.color("blue")
    elif i%4==3:
        t.color("orange")      
    t.forward(i)        
    t.right(91)         

