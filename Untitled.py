#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy  as np
import numpy  as np
type([1,2,3,4])
a=np.array([1,2,3,4])
type(a)
A=[[1,2,3],[4,5,6]]
type(A)
b=np.array(A)
print(b)
type(b)
b.ndim


# In[3]:


#Initialize array     
arr1 = [1, 2, 3, 4, 5];     
     
#Create another array arr2 with size of arr1    
arr2 = [None] * len(arr1);    
     
#Copying all elements of one array into another    
for i in range(0, len(arr1)):    
    arr2[i] = arr1[i];     
     
#Displaying elements of array arr1     
print("Elements of original array: ");    
for i in range(0, len(arr1)):    
   print(arr1[i]),    
     
print();    
     
#Displaying elements of array arr2     
print("Elements of new array: ");    
for i in range(0, len(arr2)):    
   print(arr2[i]),  

