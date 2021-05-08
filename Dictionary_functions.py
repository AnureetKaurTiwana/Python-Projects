#!/usr/bin/env python
# coding: utf-8

# In[2]:


# dictionary is a key value pair
dict_1={'a':1,'b':2,'c':3,'d':4,'e':5}
print(dict_1)
print(dict_1['a'])


# In[5]:


#length function
print('length of dictionary',len(dict_1))
list_1=[1,2,3]
print('length of the list is=',len(list_1))
string_1='anu'
print('length of the string =',len(string_1))


# In[7]:


# in function checks whether key is present or not
print('a' in dict_1)
print( 1 in dict_1)
print(1 in list_1)
print('a' in string_1)


# In[9]:


# value function

val=dict_1.values()
print('list of values of a dictionary: ',val)
print(1 in val)


# In[12]:


f=open('word.txt')
print('file opened successfully')

def word_func():
    word_dict=dict()
    for line in f:
        print(line)
        word=line.strip()
        word_dict[word]=word
    return word_dict
print(word_func().values())


# In[20]:


#looping dictionary
dict_1={'b':2,'a':1,'d':4,'c':3}
def print_hist(dict_1):
    keys_1=list(dict_1.keys())
    print(keys_1)
    keys_1.sort()
    for i in keys_1:
        print(i, dict_1[i])
print_hist(dict_1)


# In[1]:


# counter

def histogram(s):
    d=dict()
    for i in s:
        if i in d:
            d[i] +=1
        else:
            d[i]=1
    return d
s='abbcddefff'
print(histogram(s))


# In[3]:


#get function two arguments( first is key and second argument is default value)
# it returns the value corresponding to key else it returns the default value
def histogram1(s):
    d=dict()
    for i in s:
        d[i]=d.get(i,0)+1
    return d
print(histogram1(s))


# In[5]:


## global variable 
# we cant modify it inside a function without declaring it

count=0
def f():
    global count
    for i in range(5):
        count +=1
f()
print(count)


# In[10]:


## if global variable is mutable 
# it can be modified without declaring, but if it need to be reaasignend then you have to modify it

dict_1=dict()
dict_2=dict()
def modify(s):
    i=0
    global dict_2
    for j in s:
        dict_1[i]=j
        i +=1
    dict_2=dict_1
modify('anureet')
print(dict_1)
print(dict_2)
    


# In[ ]:




