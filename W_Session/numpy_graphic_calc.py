import random
import turtle as t
import numpy as np
import matplotlib.pyplot as plt

def draw_manu():
    xcor=-200
    ycor=-175
    t.penup()
    t.goto(xcor,ycor)
    t.pendown()
    draw_cmd_area()
    t.penup()
    t.goto(xcor+40,ycor-17)
    t.penup()
    t.write("madd")
    xcor=xcor+100
    
    t.penup()
    t.goto(xcor,ycor)
    t.pendown()
    draw_cmd_area()
    t.penup()
    t.goto(xcor+40,ycor-17)
    t.penup()
    t.write("msub")
    xcor=xcor+100
    
    t.penup()
    t.goto(xcor,ycor)
    t.pendown()
    draw_cmd_area()
    t.penup()
    t.goto(xcor+40,ycor-17)
    t.penup()
    t.write("msum")
    xcor=xcor+100
    
    t.penup()
    t.goto(xcor,ycor)
    t.pendown()
    draw_cmd_area()
    t.penup()
    t.goto(xcor+40,ycor-17)
    t.penup()
    t.write("msqrt")
    xcor=xcor-300
    ycor=ycor+25
    
    t.penup()
    t.goto(xcor,ycor)
    t.pendown()
    draw_cmd_area()
    t.penup()
    t.goto(xcor+5,ycor-17)
    t.penup()
    t.write("mmult_elementwise")
    xcor=xcor+100
    
    t.penup()
    t.goto(xcor,ycor)
    t.pendown()
    draw_cmd_area()
    t.penup()
    t.goto(xcor+5,ycor-17)
    t.penup()
    t.write("mmult_dot_product")
    xcor=xcor+100
    
    t.penup()
    t.goto(xcor,ycor)
    t.pendown()
    draw_cmd_area()
    t.penup()
    t.goto(xcor+20,ycor-17)
    t.penup()
    t.write("mtranspose")
    xcor=xcor+100
    
    t.penup()
    t.goto(xcor,ycor)
    t.pendown()
    draw_cmd_area()
    t.penup()
    t.goto(xcor+42,ycor-17)
    t.penup()
    t.write("minv")
    xcor=xcor-300
    ycor=ycor+25
    
    t.penup()
    t.goto(xcor,ycor)
    t.pendown()
    draw_cmd_area()
    t.penup()
    t.goto(xcor+20,ycor-17)
    t.penup()
    t.write("magic_square")
    xcor=xcor+100
    
    t.penup()
    t.goto(xcor,ycor)
    t.pendown()
    draw_cmd_area()
    t.penup()
    t.goto(xcor+42,ycor-17)
    t.penup()
    t.write("sin")
    xcor=xcor+100
    
    t.penup()
    t.goto(xcor,ycor)
    t.pendown()
    draw_cmd_area()
    t.penup()
    t.goto(xcor+42,ycor-17)
    t.penup()
    t.write("cos")
    xcor=xcor+100
    
    t.penup()
    t.goto(xcor,ycor)
    t.pendown()
    draw_cmd_area()
    t.penup()
    t.goto(xcor+45,ycor-17)
    t.penup()
    t.write("quit")
    xcor=xcor+100
    
def draw_cmd_area():
    t.forward(100)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(25)
    t.right(90)
    
def draw_screen():
    t.penup()
    t.goto(-200,-200)
    t.pendown()
    for i in range(4):
        t.forward(400)
        t.left(90)
        
def screen_clear(x,y):
    t.clear()
    t.color('black')
    t.width(1)
    draw_screen()
    draw_menu()
    
def draw_pos(x,y):
    
    if(y>=-200) and (y<=-150):
        N=int(input("Square Matrix 크기를 입력하세요:"))
        a=np.random.randint(10,size=(N,N))
        b=np.random.randint(10,size=(N,N))

    if(y>=-200) and (y<=-175):
        if (x>=-200) and (x<=-100):
            output(a,b,0)
            madd(a,b)
        elif(x>=-100) and (x<=0):
            output(a,b,0)
            msub(a,b)
        elif(x>=0) and (x<=100):
            output(a,b,1)
            msum(a)
        elif (x>=100) and (x<=200):
            output(a,b,1)
            msqrt(a)
            
    elif(y>=-175) and (y<=-150):
        if (x>=-200) and (x<=-100):
            output(a,b,0)
            mmult_elementwize(a,b)
        elif(x>=-100) and (x<=0):
            output(a,b,0)
            mmult_dot_product(a,b)
        elif(x>=0) and (x<=100):
            output(a,b,1)
            mtranspose(a)
        elif (x>=100) and (x<=200):
            output(a,b,1)
            minv(a)
            
    elif(y>=-150) and (y<=-125):
        if (x>=-200) and (x<=-100):
            magic_square()
        elif(x>=-100) and (x<=0):
            sin()
        elif(x>=0) and (x<=100):
            cos()
        elif (x>=100) and (x<=200):
            t.bye()
            


        
def output(a,b,c):
    if c==0:
        print('a matrix')
        print(a)
        print('\n')
        print('b matrix')
        print(b)
        print('\n')
    if c==1:
        print('a matrix')
        print(a)
        print('\n')        
    
def madd(a,b):
    print("a+b")
    print(np.add(a,b),'\n')

def msub(a,b):
    print("a-b")
    print(np.subtract(a,b),'\n')

def msum(a):
    print("sum(a)")
    print(np.sum(a),'\n')

def msqrt(a):
    print('sqrt(a)')
    print(np.sqrt(a),'\n')

def mmult_elementwize(a,b):
    print("a*b")
    print(np.multiply(a,b),'\n')

def mmult_dot_product(a,b):
    print("Matrix 곱 a*b")
    print(np.dot(a,b),'\n')

def mtranspose(a):
    print("transpose of a")
    print(a.transpose(),'\n')

def minv(a):
    print("inverse of a")
    print(np.linalg.inv(a),'\n')
    print("inverse of a x dpt product a")
    print(np.dot(a,np.linalg.inv(a)),'\n')

def magic_square():
    odd_flag=0
    while odd_flag!=1:
        M=int(input("Square Matrix 크기를 입력하세요:"))
        if M%2==0:
            print("홀수를 입력하세요")
        else:
            magic_square=np.zeros((M,M), dtype=int)
            odd_flag=1
    
    n=1
    i,j=0,M//2

    while n<=M**2:
        magic_square[i,j]=n
        n=n+1
        newi, newj=(i-1)%M,(j+1)%M
        if magic_square[newi,newj]:
            i=i+1
        else:
            i,j=newi,newj
    print('\n Magic Square\n',magic_square)   
       
    row_sum=0
    col_sum=0
    diag_sum=0

    for i in range(M):
        row_sum=row_sum+magic_square[0,i]
        col_sum=col_sum+magic_square[i,0]
        diag_sum=diag_sum+magic_square[i,i]

    print('\n Magic Square Row Sum:',row_sum)
    print('\n Magic Square Col Sum:',col_sum)
    print('\n Magic Square Diag Sum:',diag_sum)
    print('\n')
        
def sin():
    x=np.arange(0,4*np.pi,0.1)
    y_sin=(np.sin(x))
    plt.plot(x,y_sin)
    plt.xlabel('x axis: x values')
    plt.ylabel('y axis: sin(x)')
    plt.title('Sine')
    plt.legend(['Sine'])
    plt.show()

def cos():
    x=np.arange(0,4*np.pi,0.1)
    y_cos=(np.cos(x))
    plt.plot(x,y_cos)
    plt.xlabel('x axis: x values')
    plt.ylabel('y axis: cos(x)')
    plt.title('Cosine')
    plt.legend(['Cosine'])
    plt.show()
    
          
        
t.setup(500,500)
t.hideturtle()

draw_screen()
draw_manu()

s=t.Screen()
t.hideturtle()
s.onscreenclick(draw_pos,1)
s.onscreenclick(screen_clear,3)
