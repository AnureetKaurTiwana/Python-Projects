#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
you already have a function named has_duplicates that takes 
a list as a parameter and returns True if there is any object that appears more than once 
in the lis'''

def has_duplicate(l):
    dict_1=dict()
    for i in l:
        if i in dict_1:
            return True
        dict_1[i]=i
    return False
l=[1,2,3,4]
print(has_duplicate(l))

