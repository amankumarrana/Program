# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 13:46:47 2018

@author: baman
"""

from  sklearn import tree
#features = [[140,'smooth'], [130,'smooth'], [150,'bumpy'], [170,'bumpy']]
#lables = ['apple', 'apple', 'orange', 'orange']
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
lables = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()

clf = clf.fit(features, lables)
print (clf.predict([[150, 0]]))
