#!/usr/bin/env python
# coding: utf-8

# In[2]:


# reverse lookup

def reverse_lookup(d,v):
    t=[]
    for i in d:
        if d[i]==v:
            t.append(i)
    return t
d={1:'a',2:'b',3:'c',4:'a',5:'a',6:'b'}
print(reverse_lookup(d,'a'))
            
            


# In[5]:


# reverse dictionary
#get function two arguments( first is key and second argument is default value)
# it returns the value corresponding to key else it returns the default value
def histogram1(s):
    d=dict()
    for i in s:
        d[i]=d.get(i,0)+1
    return d
def reverse_dict(d):
    reverse=dict()
    for i in d:
        val=d[i]
        if val not in reverse:
            reverse[val]=[i]
        else:
            reverse[val].append(i)
    return reverse
s='abbcddefff'
d=histogram1(s)
print(d)
print(reverse_dict(d))

    


# In[ ]:




