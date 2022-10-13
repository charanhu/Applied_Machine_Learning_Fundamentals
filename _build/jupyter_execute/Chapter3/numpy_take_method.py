#!/usr/bin/env python
# coding: utf-8

# # Numpy take() Method

# To take elements from a NumPy array at specific indices, we use the take() function of the NumPy library. 
# 
# The take() function takes two arguments: the array and the indices of the elements to be taken. 
# 
# The indices can be passed as a list or a NumPy array. 
# 
# The take() function returns a new array with the elements taken from the original array at the specified indices.

# ## NumPy take()

# In[1]:


# Example: NumPy take()
import numpy as np
a = np.array([4, 3, 5, 7, 6, 8])
indices = [0, 1, 4]
np.take(a, indices)


# ## NumPy take() along an axis

# In[2]:


# Example: NumPy take() along an axis 1
a = np.array([[4, 3, 5], 
                [7, 6, 8]])

indices = [1]

np.take(a, indices, axis=1)


# In[3]:


# Example: NumPy take() along an axis 0
a = np.array([[4, 3, 5],
                [7, 6, 8]])

indices = [1]

np.take(a, indices, axis=0)

