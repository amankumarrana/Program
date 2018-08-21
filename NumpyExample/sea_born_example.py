# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 13:13:44 2018

@author: baman
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

x = np.linspace(1, 7, 50)
#print(x)

y = 3 + 2*x + 1.5 * np.random.rand(len(x))

df = pd.DataFrame({'XData':x, 'YData':y})
sns.regplot('XData', 'YData', data=df)
plt.show()
