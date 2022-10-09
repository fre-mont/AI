# 학생들의 신장과 체중을 받아서 성별을 출력하는 퍼셉트론
## x1(학생의 신장) , x2(학생의 체중), y (성별_남/여)
from matplotlib import test
import numpy as np
import matplotlib.pyplot as plt 
# 특징 데이터 : [x1, x2] 
X = np.array([[160, 55],
             [163, 43],
             [165, 48],
             [170, 80],
             [175, 76],
             [180, 70]])

# 라벨 데이터 : 여자는 0, 남자는 1
y = np.array([0, 0, 0, 1, 1, 1])

# 가중치 벡터 : 1로 초기화 
W = np.ones(len(X[0])) 

# 활성화 함수 : 계단함수 사용(활성값이 0보다 크면 1 반환)
def step_func(t):
    if t > 0: return 1
    else : return 0
    
# 퍼셉트론 학습 알고리즘
def perceptron_fit(X, y, epochs=10):
    global W
    eta = 0.2 # 학습률 
    
    # epochs 수만큼 학습 진행
    for i in range(1, epochs+1):
        print("-"*60)
        print("epoch :", i)
        for i in range(len(X)):
            predict = step_func(np.dot(X[i], W))
            error = y[i] - predict # 오차(예측값과 정답의 차이)
            W += eta*error*X[i] # 가중치 업데이트
            print(f'입력 : {X[i]}, 정답 : {y[i]}, 출력 : {predict}, 변경된 가중치 : {W}')
            

perceptron_fit(X, y, 20)