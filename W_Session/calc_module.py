import numpy as np

class My_calc:
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def add(self):
        c=self.a+self.b
        print('a=',self.a,'b=',self.b,'a+b=',c)
    def sub(self):
        c=self.a-self.b
        print('a=',self.a,'b=',self.b,'a-b=',c)
    def mult(self):
        c=self.a*self.b
        print('a=',self.a,'b=',self.b,'a*b=',c)
    def div(self):
        c=self.a/self.b
        print('a=',self.a,'b=',self.b,'a/b=',c)

class My_numpy_calc:
    
    def __init__(self,N):
        self.a=np.random.randint(10,size=(N,N))
        self.b=np.random.randint(10,size=(N,N))
        
    def madd(self):
        print('a:\n',self.a)
        print('b:\n',self.b)
        print("a+b:")
        print(np.add(self.a,self.b),'\n\n')
        print('-'*40)
        
    def msub(self):
        print('a:\n',self.a)
        print('b:\n',self.b)
        print("a-b:")
        print(np.subtract(self.a,self.b),'\n')
        print('-'*40)
        
    def mmult_elementwise(self):
        print('a:\n',self.a)
        print('b:\n',self.b)
        print("a*b:")
        print(np.multiply(self.a,self.b),'\n')
        print('-'*40)
        
    def mmult_dot_product(self):
        print('a:\n',self.a)
        print('b:\n',self.b)
        print("Matrix 곱 a*b:")
        print(np.dot(self.a,self.b),'\n')
        print('-'*40)