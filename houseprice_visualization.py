import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

print(train['SalePrice'].describe())


fig = plt.figure(figsize = (18, 6))

plt.subplot2grid((2, 3), (0, 0))
sns.distplot(train['SalePrice'])
plt.title('Sale Price')
plt.xlim(0, 250000)

plt.subplot2grid((2, 3), (0, 1))
var = 'GrLivArea'
vary = 'SalePrice'
data = pd.concat([train['SalePrice'], train[var]], axis=1)
#data.plot.scatter(x = var, y='SalePrice', ylim = (0, 800000))
ax = sns.scatterplot(x=var, y=vary, data=data)
plt.title('GrLivArea against Saleprice')

plt.subplot2grid((2, 3), (0, 2))
var = 'TotalBsmtSF'
data = pd.concat([train['SalePrice'], train[var]], axis=1)
#data.plot.scatter(x=var, y='SalePrice', ylim= (0, 800000))
ax = sns.scatterplot(x=var, y=vary, data = data)
plt.title('TotalBsmtSf against Saleprice')

plt.subplot2grid((2, 3), (1, 0))
var = 'MSZoning'
data = pd.concat([train['SalePrice'], train[var]], axis=1)
ax = sns.scatterplot(x=var, y=vary, data = data)
plt.title('MSZoning against Salesprice')

plt.subplot2grid((2, 3), (1, 1))
var = 'HouseStyle'
data = pd.concat([train['SalePrice'], train[var]], axis=1)
ax = sns.scatterplot(x=var, y=vary, data=data)
plt.title('Housestyle vs SalePrice')

plt.subplots_adjust(wspace=0.3, hspace=0.4)
plt.show()
