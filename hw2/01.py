# 아파트 면적을 입력하면 아파트 가격이 출력되는 시스템 
# 머신러닝 > 선형 회귀 사용 (연속적인 값 예측)

from sklearn import linear_model
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 선형 회귀 모델 생성 
lr = linear_model.LinearRegression()

# 아파트 면적과 가격 데이터 
X = [[7], [19], [31], [45], [51], [62.5], [76], [81], [88], [100], [105], [112.5], [120], [130], [147], [155], [162], [172]]
y = [5, 3, 5, 7, 11, 13, 14, 16, 19, 21, 22, 24, 25, 28, 27, 28, 30, 33]

# 학습데이터로 모델 학습
lr.fit(X,y)

# 사용자의 입력값을 받아, 모델로 예측하기 
x_new = float(input("아파트 면적을 입력하세요: "))
pred = float(lr.predict([[x_new]]))
print(f'아파트 가격은 {pred:0.2f}입니다')

# 시각화 
# W = lr.coef_
# b = lr.intercept_
# plt.scatter(X, y, color='red')
# plt.plot(X, W*X+b, color='black')
# plt.show()
