# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 16:19:04 2018

@author: baman
"""
import numpy as np
def income_tax_expenses(data):
    """
    Find the sum of positive number and the sum of negative ones
    """
    income = np.sum(data[data>0])
    expenses = np.sum(data[data<0])
    return (income, expenses)

if __name__ == '__main__':
    testData= np.array([-5, 12, 3, -6, -4, 8])
    if testData[0] < 0:
        print("Your first transaction was loss and will be dropped")
        testData = np.delete(testData, 0)
    else:
        print("Congratulation : Your first transaction was a gain")
    (my_income, my_expenses) = income_tax_expenses(testData)
    print("You have earned {0:5.2f} EUR, and spent {1:5.2f} EUR.".format(my_income, my_expenses))