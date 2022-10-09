## 랜덤수로 10x10 행렬 생성 후 최소, 최대값 구하기
## max(), min() 함수 사용 

import numpy as np

np.random.seed(0)
my_matrix = np.random.rand(10,10)
max_value = my_matrix.max()
min_value = my_matrix.min()
print(f'최소값 = {min_value} 최대값 = {max_value}')





