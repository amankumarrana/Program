# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 11:55:55 2018

@author: baman
"""

def hashing_function(key):
    """
    This function will implement has table type data structure.
    """
    hash_table = [None] * 10
    return key % len(hash_table)

def insert(hash_table, key, value):
    hash_key = hashing_function(key)
    hash_table[hash_key] = value

hash_table = [None] * 10
insert(hash_table, 10, 'Nepal')
# In the example code above, we have inserted items Nepal and USA with key 10 and 25 respectively. If we try to insert a new item with key 20 then the collision occurs because our hashing function will generate slot 0 for key 20. But, slot 0 in the hash table has already been assigned to item ‘Nepal’.
insert(hash_table, 20, 'India')
insert(hash_table, 25, 'USA')
    
hash_table_new = [[] for _ in range(10)]

def avoid_overriting_insert(hash_table_new, key, value):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table_new[hash_key]
    for i, kv in enumerate(bucket):
        k,v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        bucket[i] = ((key,value))
    else:
        bucket.append((key, value))
avoid_overriting_insert(hash_table_new, 10, 'Nepal')
avoid_overriting_insert(hash_table_new, 20, 'India')
avoid_overriting_insert(hash_table_new, 25, 'USA')

def search_from_hash_table(has_table_new, key):
    hash_key = hash(key) % len(hash_table)
    bucket = hash_table_new[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return v
print(search_from_hash_table(hash_table_new, 10))
print(search_from_hash_table(hash_table_new, 20))
print(search_from_hash_table(hash_table_new, 25))    

def delete_from_hash_table(hash_table_new, key):
    hash_key = hash(key) % len(hash_table_new)
    key_exists = False
    
    bucket = hash_table_new[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        del bucket[i]
        print('Key {} deleted'.format(key))
    else:
        print('Key {} not found in hash table'.format(key))
delete_from_hash_table(hash_table_new, 10)