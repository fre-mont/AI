# 신장과 체중데이터로 성별을 출력하는 퍼셉트론 => x1(학생의 신장) , x2(학생의 체중), y (성별_남/여)
from matplotlib import test
import numpy as np
import matplotlib.pyplot as plt 

# 특징 데이터 : [x1, x2, x0] (x0은 바이어스 입력을 위함) 
X = np.array([[160, 55, 1], [163, 43, 1], [165, 48, 1],   # -46  -35
             [170, 80, 1], [175, 76, 1], [180, 70, 1]])   # 43.8

y = np.array([0, 0, 0, 1, 1, 1])  # 정답 데이터 : 여자는 0, 남자는 1
W = np.array([1.0, 1.0, 0])  # 가중치는 [-1.0, 1.0], 바이어스 0으로 초기화 

# 활성화 함수 : 계단함수 사용
def step_func(t):
    if t > 0: return 1
    else : return 0
    
# 퍼셉트론 학습 알고리즘
def perceptron_fit(X, y, epochs=20):
    global W
    eta = 0.2 # 학습률 
    for i in range(1, epochs+1):
        print("-"*80)
        print("epoch :", i)
        for i in range(len(X)):
            predict = step_func(np.dot(X[i], W))
            error = y[i] - predict # 오차(예측값과 정답의 차이)
            W += eta*error*X[i] # 가중치 업데이트   
            print(f'정답 : {y[i]}, 출력 : {predict}, 변경된 가중치 : {W}')
            
perceptron_fit(X, y)


print(W)







