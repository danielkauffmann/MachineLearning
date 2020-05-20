import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('model_data.csv')
x = df.iloc[:, [1, 3, 4, 5, 6]].values
y = df.iloc[:, 2].values
plt.style.use('fivethirtyeight')
z = np.abs(stats.zscore(df.iloc[:, 1:]))
df = df[(z < 3).all(axis=1)]
scaler = StandardScaler()
scaler.fit_transform(x)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
model = LinearRegression(normalize=True)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print(model.score(x_test, y_test))
print(mean_squared_error(y_pred, y_test))
