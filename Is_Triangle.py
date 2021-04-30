#!/usr/bin/env python
# coding: utf-8

# In[6]:


'''Can traingle for formed with the given three sides of a rectangle
    a+b>c
    where a,b,c are the sides of a triangle'''
def is_triangle(a,b,c):
    if a+b<c or a+c<b or b+c<a:
        print("triangle not possible")
    elif a+b==c:
        print("Triangle is degenerate")
    else:
        print("Triangle is non degenerate")
a=int(input("enter side a"))
b=int(input("enter side b"))
c=int(input("enter side c"))
is_triangle(a,b,c)


# In[ ]:




