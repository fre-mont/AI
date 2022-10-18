# 아파트 면적을 입력하면 아파트 가격이 출력되는 시스템 : 머신러닝 > 선형 회귀 사용 

# 필요한 라이브러리 불러오기 
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 선형 회귀 모델 생성 
lr = linear_model.LinearRegression()

# 아파트 면적과 가격 데이터 
X = [[7], [19], [31], [45], [51], [62.5], [76], [81], [88], [100], 
     [105], [112.5], [120], [130], [147], [155], [162], [172]]
y = [5, 3, 5, 7, 11, 13, 14, 16, 19, 21, 22, 24, 25, 28, 27, 28, 30, 33]

# 학습데이터로 모델 학습
lr.fit(X,y)

# 사용자의 입력값을 받아, 모델로 예측하기 
x_new = float(input("아파트 면적을 입력하세요: "))
pred = lr.predict([[x_new]])

# 결과 화면 출력
print(f'아파트 가격은 {float(pred):0.2f}입니다')

# 예측 결과 시각화 
plt.scatter(x_new, pred)
plt.scatter(X, y, color='red')
plt.plot(X, lr.coef_*X+lr.intercept_, color='black')
plt.show()










