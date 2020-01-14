#로또 번호 추출기 만들기 프로그램

from random import shuffle
from time import sleep
game_num=input('로또 게임 횟수를 입력하세요:')
for i in range(int(game_num)):
    balls=[x+1 for x in range(45)]
    result=[]
    for j in range(6):
        shuffle(balls)
        number=balls.pop()
        result.append(number)
    result.sort()
    print('로또번호[%d]:'%(i+1),end='')
    print(result)
    sleep(1)