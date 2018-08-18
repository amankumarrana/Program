# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 18:54:52 2018

@author: baman
"""
from queue_program import Queue

def hot_potato(name_list, num):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)
    
    while(sim_queue.size() > 1):
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        sim_queue.dequeue()
    return sim_queue.dequeue()
