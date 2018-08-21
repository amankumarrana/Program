# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 13:23:37 2018

@author: baman
"""

import pandas as pd
import numpy as np
excel_file = 'data\GLM_data\GLM_data\Table 2.8 Waist loss.xls'
xls_content = pd.read_excel(excel_file)
#print(xls_content[-5:])

data = np.loadtxt('data\data.txt', delimiter=',')
#print(data)

df = pd.read_csv('data\datacomplex.txt', delimiter='[ ,]*')
#print(df)

data = np.round(np.random.randn(100,7), 2)
df = pd.DataFrame(data, columns=['Time', 'PosX', 'PosY', 'PosZ', 'VelX', 'VelY', 'VelZ'])
print(df.head())