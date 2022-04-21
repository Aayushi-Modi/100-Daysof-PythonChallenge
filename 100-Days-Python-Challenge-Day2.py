#!/usr/bin/env python
# coding: utf-8

# #Question 3
# 
# To validate whether sequence is correct?
# 

# In[1]:


def check(str1):
    result = False
    b_dict = {"{":"}", "[":"]", "(":")"}
    for i in range(len(str1)):
        j = len(str1)-i-1
        print(i, j)

        if j>i:
            if b_dict[str1[i]] == str1[j]:
                result = True
                continue
            else:
                result = False
                break
    
    return result


# In[2]:


check("{[[[]]]}")


# In[ ]:




