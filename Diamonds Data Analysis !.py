import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

diamond = pd.read_csv('diamond.csv')
print(diamond.head())

# Data Manipulation !
print(diamond[diamond['cut']=="Good"])
print(diamond[diamond['price']>5000])

print(diamond[diamond['cut']=="Premium"])
print(diamond[diamond['price']>15000])

print(diamond[diamond['cut']=="Ideal"])
print(diamond[diamond['price']<10000])

print(diamond[diamond['x']<4])

print(diamond[diamond['color']=='D'])

# Data Visualization !

plt.hist(diamond['price'],color='b')
plt.show()

plt.scatter(x='x',y='y',data=diamond,color='purple')
plt.show()




x = diamond[['carat']]
y = diamond[['price']]

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

print(x_train.head())
print(x_test.head())
print(y_train.head())
print(y_test.head())

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
print(lr.fit(x_train,y_train))
print(lr.predict(x_test)[0:5])
print(y_test.head())