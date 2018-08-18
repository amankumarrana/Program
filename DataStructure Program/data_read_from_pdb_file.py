# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 14:39:46 2018

@author: baman
"""

from operator import itemgetter
input_file = open("Data\data.pdb")
output_file = open("Data\data_test.csv","w")
table = []
header = input_file.readline()
for line in input_file:
    print line