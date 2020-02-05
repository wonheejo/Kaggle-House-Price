import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
dfs = [train, test]
#print(train.info())

# Using shape function to get an idea of the number of rows and columns there are in this data
print('Number of training examples = {}' .format(train.shape[0]))
print('Number of training columns = {}' .format(train.shape[1]))
print('Number of test examples = {}' .format(test.shape[0]))
print('Number of test columns = {}' .format(test.shape[1]))

