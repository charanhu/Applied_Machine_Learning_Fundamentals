#!/usr/bin/env python
# coding: utf-8

# # Python Dictioanry get() Method
# The get() method returns the value of the item with the specified key if the key exists. If the key does not exist, it returns the specified default value if specified, otherwise None.

# Syntax: dict.get(key, default_value)
# 
# Parameters:
# 1. key: key to be searched in the dictionary
# 2. default_value: Value to be returned if the key is not found.
# 
# The default_value parameter is optional.

# In[1]:


# Example

locations = {'meeting1':'room1', 'meeting2':'room2'}

print(locations.get('meeting1', 'online'))
# Output: room1


# Default value will be returned if the key is not found

# In[2]:


# to get the default value will be returned if the key is not found
print(locations.get('meeting3', 'online'))
# Output: online


# In[ ]:




