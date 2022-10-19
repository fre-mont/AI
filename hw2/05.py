import matplotlib.pyplot as plt
import numpy as np

eta = [0.01, 0.05, 0.1, 0.5, 1.0]  # 학습률
max_iterations = 100  # 반복횟수 

# 오차함수와 1차 도함수
def cost_func(x): return x*x-6*x+4
def gradient(x): return 2*x - 6

point = []

# 가중치 업데이트 
for t in eta:
    x = 10
    for i in range(max_iterations):
        x = x - t*gradient(x)
        point.append(x)  # 변경된 가중치 저장

arr = np.array(point)  

# 그래프 시각화
for i in range(1, len(eta) + 1):
    plt.plot(cost_func(np.arange(11)), 'b')
    plt.title(f'learning rate: {eta[i-1]}')
    
    plt.scatter(arr[(i-1)*max_iterations:i*max_iterations],
                cost_func(arr[(i-1)*max_iterations:i*max_iterations]), color='r')
    plt.show()




