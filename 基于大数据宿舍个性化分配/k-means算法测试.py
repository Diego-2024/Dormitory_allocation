import pandas as pd
from 聚类算法 import *


data = pd.read_excel('模拟宿舍分配.xlsx')

numeric_data = data.iloc[:, 3:].values
a = JuLei(numeric_data)
print(a)