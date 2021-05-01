#!/usr/bin/env python
# coding: utf-8

# In[5]:


'''Newton's method to find square root
y=(x+a/x)/2
enter the number =3
enter the estimate value=1
1
2.0
1.75
1.7321428571428572
1.7320508100147274'''
from math import*
a=int(input('enter the number ='))
x=int(input('enter the estimate value='))
while True:
    print (x)
    y=(x+a/x)/2
    if abs(x-y)<0.000001:
        break
    x=y


# In[ ]:





# In[ ]:




