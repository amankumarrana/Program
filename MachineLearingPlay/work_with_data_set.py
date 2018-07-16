# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 14:05:46 2018

@author: baman
"""

from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target

from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5)

from sklearn import tree

my_classifier = tree.DecisionTreeClassifier()

my_classifier.fit(X_train, y_train)

predictions = my_classifier.predict(X_test)

print(predictions)
from sklearn.metrics import accuracy_score

print(accuracy_score(y_test, predictions))