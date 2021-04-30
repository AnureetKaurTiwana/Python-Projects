#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''Farmet theorem 
    a^n+b^n=c^n
    This statement is not true for n>2'''
from math import *
def check_Fermat():
    a=int(input('enter first digit\n'))
    b=int(input('enter second digit\n'))
    c=int(input('enter third digit\n'))
    n=int(input('enter the value of n greater than 2='))
    if pow(a,n)+pow(b,n)==pow(c,n):
        print('Damn Framet is so wrong')
    else:
        print("opps Framet is so right")
check_Fermat()


# In[ ]:




