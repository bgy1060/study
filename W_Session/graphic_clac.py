import random
import turtle as t
import math
import sys

def draw_manu():
    xcor=-400
    ycor=-350
    t.penup()
    t.goto(xcor,ycor)
    t.pendown()
    draw_cmd_area()
    t.penup()
    t.goto(xcor+80,ycor-34)
    t.penup()
    t.write("ADD")
    xcor=xcor+200
    
    t.penup()
    t.goto(xcor,ycor)
    t.pendown()
    draw_cmd_area()
    t.penup()
    t.goto(xcor+80,ycor-34)
    t.penup()
    t.write("SUB")
    xcor=xcor+200
    
    t.penup()
    t.goto(xcor,ycor)
    t.pendown()
    draw_cmd_area()
    t.penup()
    t.goto(xcor+80,ycor-34)
    t.penup()
    t.write("MULT")
    xcor=xcor+200
    
    t.penup()
    t.goto(xcor,ycor)
    t.pendown()
    draw_cmd_area()
    t.penup()
    t.goto(xcor+80,ycor-34)
    t.penup()
    t.write("DIV")
    xcor=xcor-600
    ycor=ycor+50
    
    t.penup()
    t.goto(xcor,ycor)
    t.pendown()
    draw_cmd_area()
    t.penup()
    t.goto(xcor+67,ycor-34)
    t.penup()
    t.write("POWER")
    xcor=xcor+200
    
    t.penup()
    t.goto(xcor,ycor)
    t.pendown()
    draw_cmd_area()
    t.penup()
    t.goto(xcor+73,ycor-34)
    t.penup()
    t.write("LOG10")
    xcor=xcor+200
    
    t.penup()
    t.goto(xcor,ycor)
    t.pendown()
    draw_cmd_area()
    t.penup()
    t.goto(xcor+57,ycor-34)
    t.penup()
    t.write("FACTORIAL")
    xcor=xcor+200
    
    t.penup()
    t.goto(xcor,ycor)
    t.pendown()
    draw_cmd_area()
    t.penup()
    t.goto(xcor+85,ycor-34)
    t.penup()
    t.write("SIN")
    xcor=xcor-600
    ycor=ycor+50
    
    t.penup()
    t.goto(xcor,ycor)
    t.pendown()
    draw_cmd_area()
    t.penup()
    t.goto(xcor+80,ycor-34)
    t.penup()
    t.write("COS")
    xcor=xcor+200
    
    t.penup()
    t.goto(xcor,ycor)
    t.pendown()
    draw_cmd_area()
    t.penup()
    t.goto(xcor+85,ycor-34)
    t.penup()
    t.write("TAN")
    xcor=xcor+200
    
    t.penup()
    t.goto(xcor,ycor)
    t.pendown()
    draw_cmd_area()
    t.penup()
    t.goto(xcor+80,ycor-34)
    t.penup()
    t.write("QUIT")
    xcor=xcor+200
    
    t.penup()
    t.goto(xcor,ycor)
    t.pendown()
    draw_cmd_area()
    t.penup()
    t.goto(xcor+68,ycor-34)
    t.penup()
    t.write("CREAR")
    xcor=xcor+200
      
def draw_cmd_area():
    t.forward(200)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(50)
    t.right(90)
    
def draw_screen():
    t.penup()
    t.goto(-400,-400)
    t.pendown()
    for i in range(4):
        t.forward(800)
        t.left(90)

def draw_pos(x,y):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    
    a=random.randint(1,10)
    b=random.randint(1,10)
    
    if(y>=-400)and (y<=-350):
        if(x>=-400)and (x<-200):
            add(a,b)
        elif (x>=-200) and (x<0):
            sub(a,b)
        elif (x>0)and (x<200):
            mult(a,b)
        elif (x>=200) and (x<400):
            div(a,b)
    elif (y>=-350)and (y<=-300):
        if (x>=-400) and (x<-200):
            power(a,b)
        elif (x>=-200) and (x<0):
            log10(a)
        elif (x>0)and (x<200):
            factorial(a)
        elif (x>=200) and (x<400):
            sin(a)
    elif (y>=-300)and (y<=-250):
        if (x>=-400) and (x<-200):
            cos(a)
        elif (x>=-200) and (x<0):
            tan(a)
        elif (x>0)and (x<200):
            t.bye()
        elif (x>=200) and (x<400):
            t.clear()

def add(a,b):
    c=a+b
    print("a=",a,"b=",b,"a+b=",c)

def sub(a,b):
    c=a-b
    print("a=",a,"b=",b,"a-b=",c)

def mult(a,b):
    c=a*b
    print("a=",a,"b=",b,"a*b=",c)

def div(a,b):
    c=a/b
    print("a=",a,"b=",b,"a/b=",c)

def power(a,b):
    c=math.pow(a,b)
    print("a=",a,"b=",b,"pow(a,b)=",c)

def log10(a):
    c=math.log10(a)
    print("a=",a,"log(a)=",c)

def factorial(a):
    c=math.factorial(a)
    print("a=",a,"fact(a)=",c)

def sin(a):
    c=math.sin(math.radians(a))
    print("a=",a,"sin(a)=",c)

def cos(a):
    c=math.cos(math.radians(a))
    print("a=",a,"cos(a)=",c)

def tan(a):
    c=math.tan(math.radians(a))
    print("a=",a,"tan(a)=",c)

def screen_clear(x,y):
    t.clear()
    t.color('black')
    t.width(1)
    draw_screen()
    draw_menu()

t.setup(1000,1000)
t.hideturtle()

draw_screen()
draw_manu()

s=t.Screen()
t.hideturtle()
s.onscreenclick(draw_pos,1)
s.onscreenclick(screen_clear,3)
