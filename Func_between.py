#!/usr/bin/env python
# coding: utf-8

# In[7]:


'''Write a function is_between(x, y, z) that returns True if x ≤ y ≤ z or False 
otherwise.
'''
from math import *
def between(x,y,z):
    return x<=y and y<=z
x=int(input('enter the value of x'))
y=int(input('enter the value of y'))
z=int(input('enter the value of z'))
if between(x,y,z):
    print('Yes y lies between x and z')
else:
    print('no y doesn\'t lie between x and y')


# In[ ]:




