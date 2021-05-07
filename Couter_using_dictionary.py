#!/usr/bin/env python
# coding: utf-8

# In[1]:


def histogram(s):
    dict_1=dict()
    for i in s:
        if i in dict_1:
            dict_1[i] +=1
        else:
            dict_1[i]=1
    return dict_1
print(histogram('aabccdeef'))


# In[ ]:




