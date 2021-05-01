#!/usr/bin/env python
# coding: utf-8

# In[8]:


n=int(input('enter the value of n'))
def fact(n):
    space=' '*(4*n)
    print(space,'factorial',n)
    if not isinstance(n,int):
        print('Factorial can be found out for integer')
        return None
    elif n<0:
        print('Factorial can be found out for integer')
        return None
    elif n==0:
        print(space,'returning',1)
        return 1    
    elif n==1:
        print(space,'returning',n)
        return 1
    else:
        print(space,'returning',n)
        result=n*fact(n-1)
        return result

print(fact(n))


# In[ ]:





# In[ ]:




