# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 14:48:23 2018

@author: baman
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.r_[0:10:0.1]
freq = 0.5
x = np.sin(2 * np.pi * freq * t)

plt.plot(t, x)
plt.xlabel('Time[sec]')
plt.ylabel('Values')
plt.savefig(r'graph_images\Sinewave.png', dpi=200)
plt.show()