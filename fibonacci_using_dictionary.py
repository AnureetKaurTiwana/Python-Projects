#!/usr/bin/env python
# coding: utf-8

# In[4]:


def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(9))
    


# In[7]:


## using dictionary 
## decrease time complexity
t={0:0,1:1}
def fibonacci(n):
    if n in t:
        return t[n]
    res=fibonacci(n-1)+ fibonacci(n-2)
    t[n]=res
    return res
print(fibonacci(1000))


# In[10]:





# In[ ]:




