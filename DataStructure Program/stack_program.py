# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:39:39 2018

@author: baman
"""

class Stack:
    """
    Creating stack class
    """
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)
        