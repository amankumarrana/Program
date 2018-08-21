# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 12:28:23 2018

@author: baman
"""

class sorting_algo:
    """
        This class will contain all type of sorting algorithm in python.
    """
    def bubble_sort(self, lyst):
        """
        It is a comparison-based algorithm in which each pair of 
        adjacent elements is compared and the elements are swapped
        if they are not in order.
        """
        for iter_num in range(len(lyst)-1, 0, -1):
            for idx in range(iter_num):
                if lyst[idx] > lyst[idx + 1]:
                    temp = lyst[idx]
                    lyst[idx] = lyst[idx + 1]
                    lyst[idx + 1] = temp
        print(lyst)
        
    def insertion_sort(self, lyst):
        """
        So in beginning we compare the first two elements
        and sort them by comparing them. 
        Then we pick the third element and 
        find its proper position among the previous two sorted elements.
        """
        for i in range(1, len(lyst)):
            j = i - 1
            next_element = lyst[i]
            while(lyst[j] > next_element) and (j>=0):
                lyst[j + 1] = lyst[j]
                j = j - 1
                lyst[j + 1] = next_element
        print(lyst)
    
    def quick_sort(self, array):
        less = []; greater = []
        if len(array) <= 1:
            return array
        pivot = array.pop()
        for x in array:
            if x <= pivot: less.append(x)
            else: greater.append(x)
        return quick_sort(less) + [pivot] + quick_sort(greater)

if __name__ == 'main':
    s = sorting_algo()
    s.bubble_sort([19,2,31,45,6,11,121,27])