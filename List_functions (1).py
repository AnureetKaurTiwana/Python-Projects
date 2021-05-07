#!/usr/bin/env python
# coding: utf-8

# In[3]:


#list is mutable
list1=['a',1,2,['b','c']]
for i in list1:
    print(i)
list1[0]=100
for i in list1:
    print(i)


# In[12]:


#update a list
for i in range(len(list1)):
    print(list1[i])
    list1[i]=list1[i]*2
    print('updated value',list1[i])


# In[15]:


#concatination of lists

list2=list1+['anu','money']
print(list2)


# In[16]:


# * operator

list2=list2*2
print(list2)


# In[17]:


# list slicing

print(list2[2:5])


# In[23]:


# list methods
#append, Extend, sort, sum,
list3=['sister','brother']
list3.append('are')
print(list3)
list3.extend(['anu'])
print(list3)


# In[24]:


list3.sort()
print(list3)


# In[25]:


# sum function

list1=[1,2,3,4,5]
result=0
for i in list1:
    result +=i
print("sum of elements=",result)
print("sum using sum function=",sum(list1))


# In[5]:


# isupper string function
#length is a method not a function
list1=['ANU','MO']
for i in list1:
    if not i.isupper():
        print('False')
        break
    if i==list1[len(list1)-1]:
        print('True')


# In[17]:


'''Write a function that takes a list of numbers and returns the cumulative sum; that is, a 
new list where the ith element is the sum of the first i+1 elements from the original list. 
For example, the cumulative sum of [1, 2, 3] is [1, 3, 6]
'''

def sum_cumulative(l):
    sum_r=0
    res=[]
    for i in range(len(l)):
        if i==0:
            res.append(l[i])
            sum_r=res[i]
        else:   
            sum_r=res[i-1]+l[i]
            res.append(sum_r)
    return res
print(sum_cumulative([1,2,3,4]))


# In[22]:


## pop , del, remove function
list1=['a',1,2,3,4,5,6,7,8,9,10]
# pop returns the value

print(list1.pop(0))
print(list1)

# remove function remove the element and take it as an argument
# it return none unlike pop
print(list1.remove(1))

#del function doest not return anything and it can use slicing instead of an index as well

del list1[3]
print(list1)

del list1[5:]

print(list1)


# In[23]:


'''
Write a function called middle that takes a list and returns a new list that contains all 
but the first and last elements. So middle([1,2,3,4]) should return [2,3].'''

def mid_last_remove(l):
    l.pop()
    l.pop(0)
    return l
print(mid_last_remove([1,2,3,4,5]))


# In[5]:


# call by reference
#objects and values
#when the list is passed as an argument it gives reference to the function, any modification will reflect to the original list.

def delete(list1):
    del list1[0:2]
list1=[1,2,3,4,5,6]
delete(list1)
print(list1)

# append method modify the list and return nothing
# contatination return new list

print(list1.append('a'))
print(list1+['anu'])

# sort method also return none and change the source itself
list2=[2,1,5,3]
print(list2.sort())
print(list2)


# In[ ]:




