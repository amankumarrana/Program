# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 18:44:19 2018

@author: baman
"""

class Queue:
    """
    This class will linear type datastructure called Queue
    """
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)
    
    def size(self):
        return len(self.items)
    
    def dequeue(self):
        return self.items.pop()
    