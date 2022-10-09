## 5x5 행렬 생성 => 체스 보드 패턴 

import numpy as np

my_matrix = np.zeros((5, 5))
my_matrix[1::2, ::2] = 1
my_matrix[::2, 1::2] = 1
print(my_matrix)


