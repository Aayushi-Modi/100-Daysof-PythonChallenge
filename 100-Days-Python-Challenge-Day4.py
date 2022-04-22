#!/usr/bin/env python
# coding: utf-8

# "Aayushi Modi", remove all the vowels from this string and return the residual string.

# In[55]:


vowel = ['a','e','i','o','u']
str1 = 'Python Programming'
str2 = str1.lower()
for i in str2:
    if i in vowel:
        continue
    else:
        print(i, end="")


# "hahlolaayuhalolhhellohehewtflol",  find the starting index of first occurance of "aayushi" in that string.

# In[56]:


str1 = "hahlolaayuhalolhhellohehewtflol"
str2 = 'hello'
if str2 in str1:
    print(str1.index(str2))


# In[ ]:




