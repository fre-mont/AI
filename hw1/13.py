## 3x3 크기의 2차원 배열 생성 => np.arange().reshape() 사용 
## 모든 요소의 합, 각 열과 행의 합 계산 => sum() 사용 

import numpy as np
my_matrix = np.arange(9).reshape(3, 3)
print(f'원본 배열: \n {my_matrix}')
print(f'모든 요소의 합: {my_matrix.sum()}')
print(f'각 행의 합: {my_matrix.sum(axis=0)}')
print(f'각 열의 합: {my_matrix.sum(axis=1)}')





