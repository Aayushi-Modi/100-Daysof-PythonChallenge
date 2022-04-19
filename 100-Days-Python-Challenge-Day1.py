#!/usr/bin/env python
# coding: utf-8

# #Question2
# 
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# In[67]:


from operator import add
list1 = [2,4,3]
list2 = [5,6,4]
list1.reverse()
list2.reverse()
print(list1,list2)
list3 = list(map(add,list1,list2))
list3.reverse()
print(list3)


# In[91]:


list1 = [2,4,3]
list2 = [5,6,4]
list3=[]
list1.reverse()
list2.reverse()
str1 = ''
str2 = ''
str1 = str1.join(map(str,list1))
str1 = int(str1)
str2 = str2.join(map(str,list2))
str2= int(str2)
str3 = str(str1+str2)
str3 = list(str3)
str3.reverse()
str3


# In[ ]:




