import numpy as np

# 특징 데이터 : [x1, x2, x0] 
X = np.array([[0, 1, 1],
             [1, 0, 1],
             [1, 2, 1],
             [2, 1, 1]])
y = np.array([0, 0, 1, 1])  # 정답 데이터
W = np.array([0, 0, -1.0])  # 가중치 

# 활성화 함수 : 계단함수 사용
def step_func(t):
    if t > 0: return 1
    else : return 0
    
# 퍼셉트론 학습 알고리즘
def perceptron_fit(X, y, epochs=5):
    global W
    eta = 1.0 # 학습률 

    for i in range(1, epochs+1):
        print("-"*60)
        print("epoch :", i)
        for i in range(len(X)):
            predict = step_func(np.dot(X[i], W))
            error = y[i] - predict # 오차(예측값과 정답의 차이)
            W += eta*error*X[i] # 가중치 업데이트
            print(f'입력 : {X[i]}, 정답 : {y[i]}, 출력 : {predict}, 변경된 가중치와 바이어스 : {W}')
            

perceptron_fit(X, y)



    
    
