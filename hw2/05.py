import matplotlib.pyplot as plt
import numpy as np

eta = 0.1
x = 10 
max_iterations = 100

cost_func = lambda x: x*x-6*x+4
gradient = lambda x: 2*x - 6


for i in range(max_iterations):
    x = x - eta* gradient(x)
    print("손실함수값(", x, ")=", cost_func(x))

print("최소값 = ", x)