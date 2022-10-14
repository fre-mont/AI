import matplotlib.pyplot as plt
import numpy as np

eta = 0.1
x = 10 
max_iterations = 100

cost_func = lambda x: x*x-6*x+4
gradient = lambda x: 2*x - 6

point = []

for i in range(max_iterations):
    x = x - eta* gradient(x)
    point.append(x)
    print("손실함수값(", x, ")=", cost_func(x))

arr = np.array(point)
print(arr)
print("최소값 = ", x)

plt.plot(cost_func(np.arange(11)), 'b')
plt.scatter(arr, cost_func(arr), color='r')
plt.show()
