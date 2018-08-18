# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 14:33:23 2018

@author: baman
"""

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def insertAfter(self, prev_node, new_data):
        
        if prev_node is None:
            print ("The Given previous node must in the linked list")
            return 
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next  = new_node
    
    def append(self, new_data):
        
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
            
        last.next = new_node
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next
    
if __name__ == '__main__':
    llist=  LinkedList()
    llist.append(6)
    llist.push(7)
    llist.push(1)
    llist.append(4)
    llist.insertAfter(llist.head.next, 8)
    print ("Created Linked List is :")
    llist.printList()