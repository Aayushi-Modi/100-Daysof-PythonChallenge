#!/usr/bin/env python
# coding: utf-8

# #1
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# In[34]:


nums = [1,2,3,4,5]
num =[]
target = 5

for i in nums:
    for k in nums:
        s= i+k 
        if s==target:
            i_new=nums.index(i)
            k_new=nums.index(k)
            print(i_new,k_new)        


# 
