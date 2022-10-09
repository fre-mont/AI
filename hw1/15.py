## 주어진 데이터로 선 그래프 그리기

import numpy as np
import matplotlib.pyplot as plt

data = np.array((2, 0, 3, 6, 4, 6, 8, 12, 10, 9, 18, 20, 22))
x_axis = np.arange(len(data)) 

plt.plot(x_axis, data)
plt.show()
