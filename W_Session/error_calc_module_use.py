#과제10_1771023_박지연_use 사례

from error_calc_module_def import My_calc
from error_calc_module_def import My_numpy_calc
import numpy as np

x=int(input('x값을 입력하세요:'))
y=int(input('y값을 입력하세요:'))
print('='*40)

c1=My_calc(x,y)
try:
    c1.div()
    
except ZeroDivisionError as e:
            print(e)
            print(type(e))
else:
    c1.add()
    c1.sub()
    c1.mult()
    

print('='*40)
N=int(input('Square Matrix 크기를 입력하세요:'))
print('='*40)

c2=My_numpy_calc(N)

try:
    c2.mdiv()

except ZeroDivisionError as e:
            print(e)
            print(type(e))
else:
    c2.madd()
    c2.msub()
    c2.mmult_elementwise()


