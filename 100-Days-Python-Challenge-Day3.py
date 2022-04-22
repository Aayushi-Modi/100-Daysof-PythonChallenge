#!/usr/bin/env python
# coding: utf-8

# Reverse a string --> 2 other methods than str1[::-1]

# In[3]:


#1 method
str1 = 'Python Programming'
list1 = list(str1)
list1.reverse()
str2 = ''.join(list1)
print(str2)


# In[4]:


#2 method
str1 ='Python Programming'
for i in reversed(range(len(str1))):
    print(str1[i], end ="")


# In[1]:


#3 method
str1 = 'Python Programming'
for i in range(len(str1)-1,-1,-1):
    print(str1[i],end ="")


# In[ ]:




