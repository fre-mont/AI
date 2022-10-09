## 넘파이 배열에 연산자를 적용하면 배열의 요소마다 연산자가 적용된다

import numpy as np
my_vector = np.array([1, 2, 3, 4, 5, 6])
selection = my_vector % 2 == 0
print(my_vector[selection])



