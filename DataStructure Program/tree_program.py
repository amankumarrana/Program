# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 13:19:58 2018

@author: baman
"""

class tree_program:
    """
    This program will implement tree data structure.
    """
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
        
    def insert_into_tree(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = tree_program(data)
                else:
                    self.left.insert_into_tree(data)
            elif data > self.data:
                if self.right is None:
                    self.right = tree_program(data)
                else:
                    self.right.insert_into_tree(data)
        else:
            self.data = data
    
    def findval(self, lkpval):
         if lkpval < self.data:
             if self.left is None:
                 return str(lkpval)+" Not Found"
             return self.left.findval(lkpval)
         elif lkpval > self.data:
             if self.right is None:
                 return str(lkpval)+" Not Found"
             return self.right.findval(lkpval)
         else:
             print(str(self.data) + ' is found')
    
            
t = tree_program(12)
t.insert_into_tree(6)
t.insert_into_tree(14)
t.insert_into_tree(3)
t.findval(3)

t.PrintTree()