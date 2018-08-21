# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 11:47:28 2018

@author: baman
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
t = np.arange(0, 10, 0.1)
x = np.sin(t)
y = np.cos(t)

df = pd.DataFrame({'Time':t, 'x':x, 'y':y})
#print(df.Time)
#print(df['Time'])
#data = df[['Time', 'y']]
#print(data.head())
#print(data.tail())
#print(data[4:10])
#print(df[['Time', 'y']][4:10])

data = pd.DataFrame({
        'Gender': ['f', 'f', 'm', 'f', 'm', 'm', 'f', 'm', 'f', 'm', 'm'],
        'TV': [3.4, 3.5, 2.6, 4.7, 4.1, 4.1, 5.1, 3.9, 3.7, 2.1, 4.3]})
#print(data)
# group the data
grouped = data.groupby('Gender')
print(grouped.describe())
grouped.boxplot()
plt.show()

# get the groups as DataFrames

df_female = grouped.get_group('f')
values_female = grouped.get_group('f').values
print(df_female)
print(values_female)