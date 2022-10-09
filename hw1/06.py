## 0~8까지의 1차원 배열
## 3x3 행렬로 변환 => reshape 함수 이용

import numpy as np
my_vector = np.arange(0, 9)
my_matrix = my_vector.reshape(3, 3)
print(my_matrix)



