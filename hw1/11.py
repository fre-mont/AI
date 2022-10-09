
## 랜덤값으로 3x3 행렬 생성
## 평균값과 표준편차 (x-mean)/std => 행렬 정규화 

import numpy as np

np.random.seed(0)
my_matrix = np.random.rand(3, 3)
mean_value = my_matrix.mean()
std_value = my_matrix.std()
my_matrix = (my_matrix - mean_value)/std_value
print(my_matrix)



