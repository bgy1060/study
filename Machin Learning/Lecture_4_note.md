# 4.인공뉴론의 동작원리

## 1).  인공뉴론의 동작 원리

  하나의 뉴론은 간단한 연산을 하는 함수처럼 작동한다. 인공뉴론의 모델은 입력에 대해 곱셈하고 합산한 후, 그 결과를 임계값과 비교하여 출력하는 것이다. 하지만 이렇게 단순한 뉴론들이 여러 개 모이면 마치 기계학습(ML)처럼 작동한다.



<img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200122162509490.png" alt="image-20200122162509490" style="zoom: 67%;" />

  

  mileToKm()함수를 기계학습(ML)에서는 y=w_1x_1으로 표현할 수 있다. 수학에서 말하는 일차함수 y=ax와 같은 형식이다. 이 함수를 그래프로 그리면, 기울기가 w_1이고, 원점을 지나는 직선이 된다. 

  기계학습(ML)에서 이러한 기울기를 가중치라고하고 영어로는 weights라고 부른다. 가중치에 의해서, 뉴론에 들어가는 입력 신호는 커지기도 하고 작아지기도 한다. 입력(x)와 가중치(y)는 하나가 아니라 여러개일 수 있다. 





<img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200122162936954.png" alt="image-20200122162936954" style="zoom:67%;" />



  뉴론에 들어오는 신호의 총합을 순입력이라고 한다. 영어로는 net inputs. 위 그림에서는 2개의 입력 신호 x에, 각각의 가중치가 곱해진 값이 순입력으로 뉴론에 입력된다. 

  만약 뉴론에 들어온 순입력의 값이 임계값(threshold)를 넘어설 때만 뉴론에서 출력이 이루어진다. 이 때, 뉴론이 활성화 되었다, activate라고 말한다. 

- 순입력(net input) : w_1*x_1 + w_2*x_1
- 입계값(threshold) : θ
- 활성화(activated) : > θ

<img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200122164108041.png" alt="image-20200122164108041" style="zoom:67%;" />

  위 식을 수식으로 나타내면 다음과 같다. 이 식에서 θ를 b라 하고 이것을 왼쪽으로 넘기면

<img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200122164228607.png" alt="image-20200122164228607" style="zoom:67%;" />

  다음과 같이 표현할 수 있다. 여기서 b를 편향(bias)라고 부른다. 위 식을 다시 그림으로 변환하면 다음과 같다.

​                               <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200122164430057.png" alt="image-20200122164430057" style="zoom: 67%;" />

  

  위 그림에서처럼 편향을 뉴론의 입력값의 한 부분으로 간주하고 계산할 수 있다. 편향은 인공 뉴론에서 항상 켜져있는 노드라고 볼 수 있다. 입력값과는 다르게, 입력값 대신에 항상 1을 편향 b에 곱하여 순입력에 더하게 된다. 

  입력값과 가중치를 각각 곱한 값과 편향을 더해서, 그 값이 0 이상이면 1이 출력되고, 그렇지 않으면 0이 출력된다. 



## 2). AND 게이트 뉴론 구현하기

​                                                              **AND 진리표**

|  x1  |  x2  |  y   |
| :--: | :--: | :--: |
|  0   |  0   |  0   |
|  0   |  1   |  0   |
|  1   |  0   |  0   |
|  1   |  1   |  1   |



  AND 게이트 뉴론을 만든다는 것은 AND 함수를 구현하는 것이다. 따라서 우리가 구현할 뉴론은 입력 x1, x2을 받아서 진리표에 제시된 것처럼, y 값을 출력하면 된다. 

<img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200122165928130.png" alt="image-20200122165928130" style="zoom:67%;" />

AND 함수는 매개변수의 입력으로 x1, x2를 받아서, w1, w2, b와 연산하여 AND 진리표를 만족하는 답을 반환하면 된다.  AND 진리표를 만족하는 w1, w2, b가 너무 많지만 본 예제에서는 w1 = 0.5, w2 = 0.5, b = -0.7 사용.

함수 안에서, 입력과 가중치를 곱할 입력 x를 넘파이 배열로 표현하면

```python
import numpy as np

def AND(x1,x2):
    x = np.array([1,x1,x2])         #input
    w = np.array([-0.7,0.5,0.5])    #bias + weight
    return int(np.dot(w,x) > 0)
```

함수가 잘 구현되었는지 확인하고 싶다면 다음 코드 이용.

```python
print('AND(0,0) = ',AND(0,0))
print('AND(0,1) = ',AND(0,1))
print('AND(1,0) = ',AND(1,0))
print('AND(1,1) = ',AND(1,1))
```

