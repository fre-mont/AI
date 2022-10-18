import matplotlib.pyplot as plt
import numpy as np

# 학습률 
eta = [0.01, 0.05, 0.1, 0.5, 1.0]
max_iterations = 100
point = []

# 오차함수와 1차 도함수
cost_func = lambda x: x*x-6*x+4
gradient = lambda x: 2*x - 6

for t in eta:
    x = 10
    for i in range(max_iterations):
        x = x - t*gradient(x)
        point.append(x)
    
arr = np.array(point)

# 그래프 시각화 
for i in range(1, len(eta) + 1):
    plt.plot(cost_func(np.arange(11)), 'b')
    plt.title(f'learning rate: {eta[i-1]}')
    plt.scatter(arr[(i-1)*100:i*100], cost_func(arr[(i-1)*100:i*100]), color='r')
    plt.show()




