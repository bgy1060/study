from random import shuffle

male=['A','B','C']
female=['D','E','F']

shuffle(male)
shuffle(female)

couples=zip(male,female)

for i,couple in enumerate(couples):
    print('커플%d: [%s]-[%s]' %(i+1,couple[0],couple[1]))

'''
<zip 함수>
- zip은 동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수이다.

<enumerate 함수>
- 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능
- enumerate는 "열거하다"라는 뜻이다. 이 함수는 순서가 있는 자료형을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴한다. 
'''