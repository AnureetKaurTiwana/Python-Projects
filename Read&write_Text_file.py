#!/usr/bin/env python
# coding: utf-8

# In[7]:


with open('file1.txt', 'a') as f:
    while True:
        f.write(input('enter line1\n'))
        f.write('\n')
        c=input('shall I stop writing then write Y else write F')
        if c=='Y':
            break
    f.close()


# In[8]:


with open('file1.txt') as f:
    content=f.read()
    print(content)
    f.close()


# In[ ]:




