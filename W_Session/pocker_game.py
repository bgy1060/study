from random import shuffle

cards=['sa','s2','s3','s4','s5','s6','s7','s8','s9','s10','sj','sq','sk', 'ha','h2','h3','h4','h5','h6','h7','h8','h9','h10','hj','hq','hk', 'da','d2','d3','d4','d5','d6','d7','d8','d9','d10','dj','dq','dk', 'ca','c2','c3','c4','c5','c6','c7','c8','c9','c10','cj','cq','ck']

player1=[]
player2=[]
player3=[]
player4=[]

shuffle(cards)

for i in range(20):
    card=cards.pop()
    if i%4==0:
        player1.append(card)
    elif i%4==1:
        player2.append(card)
    elif i%4==2:
        player3.append(card)
    elif i%4==3:
        player4.append(card)
   
player1.sort()
player2.sort()
player3.sort()
player4.sort()

print("player1 card=",player1)
print("player2 card=",player2)
print("player3 card=",player3)
print("player4 card=",player4)