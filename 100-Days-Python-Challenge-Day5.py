#!/usr/bin/env python
# coding: utf-8

# Rotate the string "Python Programming" by 'n' input to the left.
# 
# Eg: n=2, rotate the string by 2 index to the left.
# Result - "ngPython Programmi"

# In[18]:


str1 = input('Enter a string: ')
n = int(input('Enter a index to rotate it: '))
str2 = str1[0:-n]
str3 = str1[-n:]
str4 = str3+str2
print(str4)


# In[ ]:




