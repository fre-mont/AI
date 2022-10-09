# 아파트 면적을 입력하면 아파트 가격이 출력되는 시스템 
# 머신러닝 > 선형 회귀 사용 (연속적인 값 예측)

import numpy as np
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 선형 회귀 모델 생성 
lr = linear_model.LinearRegression()

# 넘파이 배열로 구성된 데이터 
X = np.array([2, 0, 3, 6, 4, 6, 8, 12, 10, 9, 18, 20, 22])
y = np.array([])

x_axis = np.arange(len(data)) 

plt.plot(x_axis, data)
plt.show()