## 0~9까지의 벡터 생성
# 5-8 사이 숫자 부호를 반전 (-1 곱하기)

import numpy as np
my_vector = np.arange(0, 10)
# 5 6 7 8에만 -1을 곱하기
my_vector[5:9] *= -1
print(my_vector)






