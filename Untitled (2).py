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


# In[5]:


arr[] = {5, 10, 30, 7}


# In[6]:


# Python program for the above approach

# Function to sort array in the way
# mentioned above
def AwesomeSort(m, n):

	# Create three vectors
	v1, v2, v3 = [],[],[]
	
	# Traverse through the elements
	# of the array
	for i in range(n):
	
		# If elements are even and
		# divisible by 10
		if (m[i] % 10 == 0):
			v1.append(m[i])

		# If number is even but not divisible
		# by 5
		elif (m[i] % 2 == 0):
			v2.append(m[i])
		else:
			# If number is odd
			v3.append(m[i])

	# Sort v1 in descending orde
	v1 = sorted(v1)[::-1]

	for i in range(len(v1)):
		print(v1[i], end = " ")

	for i in range(len(v2)-1,-1,-1):
		print(v2[i], end = " ")

	for i in range(len(v3)):
		print (v3[i], end = " ")

# Driver Code
if __name__ == '__main__':

	# Given Input
	arr = [5, 10, 30, 7]
	N = len(arr)

	# FunctionCall
	AwesomeSort(arr, N)

	# This code is contributed by mohit kumar 29.


# In[7]:


# Python Program illustrating
# numpy.reshape() method

import numpy as geek

# array = geek.arrange(8)
# The 'numpy' module has no attribute 'arrange'
array1 = geek.arange(8)
print("Original array : \n", array1)

# shape array with 2 rows and 4 columns
array2 = geek.arange(8).reshape(2, 4)
print("\narray reshaped with 2 rows and 4 columns : \n",
	array2)

# shape array with 4 rows and 2 columns
array3 = geek.arange(8).reshape(4, 2)
print("\narray reshaped with 4 rows and 2 columns : \n",
	array3)

# Constructs 3D array
array4 = geek.arange(8).reshape(2, 2, 2)
print("\nOriginal array reshaped to 3D : \n",
	array4)

