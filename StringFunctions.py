#!/usr/bin/env python
# coding: utf-8

# In[6]:


index=-1
string=input('enter the string')
length=len(string)
print(length)
while index>=(-length):
    print(string[index])
    index=index-1
for i in string:
    print(i)


# In[7]:


#count function
string='banana'
count=string.count('an')
print(count)


# In[12]:


#find function
find=string.find('na',3)
print(find)
#not found the string it returns -1
find=string.find('na',6,6)
print(find)


# In[13]:


# in function which is a boolean
string1='anureet'
string2='anu'
print(string2 in string1)


# In[20]:


#relational operators
word='anuree'
if word<string1:
    print('your word '+word+' comes before '+string1)
elif word>string1:
    print('your word '+word+' comes after '+string1)
else:
    print('your word '+word+' is '+ string1)


# In[23]:


#reverse function
string1=input('enter string1')
string2=input('enter string2')
len1=len(string1)
len2=len(string2)
print('len1='+str(len1)+',len2='+str(len2))
def check_reverse(string1,string2):
    j=0
    i=-1
    if len1==len2:
        while j<len1:
            if string1[j]==string2[i]:
                j=j+1
                i=i-1
            else:
                return False
            if j==len1:
                return True
    else:
        return False
print(check_reverse(string1,string2))

#method2 
if string1==string2[::-1]:
    print("its true")
else:
    print("its false")


# In[25]:


#slicing
# return reverse take -1 step means start from last
#2 means until index2
print(string1[::-1])
print(string1[:2:])


# In[27]:


# is_lower function
print(string1.islower())
print(string2.islower())


# In[33]:


order=ord('a')
print(order)
letter=chr(97)
print(letter)
#shift the string by the given value
value=int(input('enter the vlaue of shift'))
string1=input('enter the string')

def shift(value, string1):
    newword=''
    for i in string1:
        if i.isupper():
            newword+=chr(normalize(ord(i)+value,65,90))
        else:
            newword+=chr(normalize(ord(i)+value,97,122))
    return newword
def normalize(x,min,max):
    if x>max:
        x-=26
    if x<min:
        x+=26
    return x
print(shift(2,'anu'))


# In[ ]:




