# 배열의 테두리에 1, 내부에 0을 가진 2차원 배열 생성
## 슬라이싱을 사용하기 

import numpy as np

my_matrix = np.ones((3, 3))
my_matrix[1:-1, 1:-1] = 0 # my_matrix[1, 1]과 동일한 결과 
print(my_matrix)

