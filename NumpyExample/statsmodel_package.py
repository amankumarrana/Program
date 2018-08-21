# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 12:38:20 2018

@author: baman
"""

import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd
from patsy import dmatrices



dat = sm.datasets.get_rdataset('Guerry', 'HistData').data
results = smf.ols('Lottery ~ Literacy +np.log(Pop1831)', data=dat).fit()
print(results.summary())
vars =['Department', 'Lottery', 'Literacy', 'Wealth', 'Region']
df = dat[vars]
#print(dat)
print(df[-5:])

df = dat.dropna()
print(df[-5:])

