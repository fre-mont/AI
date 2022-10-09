# 넘파이 배열끼리 연산을 할 때, 크기가 다르면 넘파이는
# 자동으로 배열의 크기를 확장 ==> 브로드캐스팅 

import numpy as np

first_matrix = np.array([[1, 2, 3], [4, 5, 6]])
second_matrix = np.array([1, 2, 3])

print(first_matrix + second_matrix)









