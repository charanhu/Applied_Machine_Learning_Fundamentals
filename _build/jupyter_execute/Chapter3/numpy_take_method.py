#!/usr/bin/env python
# coding: utf-8

# # Numpy take() Method

# To take elements from a NumPy array at specific indices, we use the take() function of the NumPy library. 
# 
# Syntax: numpy.take(array, indeices, axis, out, mode)
# 
# Parameters:
# 1. array: Input array
# 2. indices: The indices of the values to extract
# 3. axis: The axis over which to select values. By default, the flattened input array is used.
# 4. out: A location into which the result is stored. If provided, it must have a shape that the indices along axis.
# 5. mode: {‘raise’, ‘wrap’, ‘clip’}, optional, Specifies how out-of-bounds indices will behave.
#     1. ‘raise’ – raise an error (default)
#     2. ‘wrap’ – wrap around
#     3. ‘clip’ – clip to the range
# 6. Returns: The returned array has the same type as array.

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

