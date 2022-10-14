#!/usr/bin/env python
# coding: utf-8

# # Python Data Types

# Difination: Data types are the classification or categorization of data items. It represents the kind of value that tells what operations can be performed on a particular data.
# 
# Python has the following data types built-in by default, in these categories:
# 
# 1. Text Type:	str
# 2. Numeric Types:	int, float, complex
# 3. Sequence Types:	list, tuple, range
# 4. Mapping Type:	dict
# 5. Set Types:	set, frozenset
# 6. Boolean Type:	bool
# 7. Binary Types:	bytes, bytearray, memoryview
# 
# ## Obtaining the Data Type
# You can get the data type of any object by using the type() function:

# In[1]:


# Example:
x = 5

print(type(x))


# ## Data Type Setting
# When you give a variable a value in Python, the data type is already determined:

# In[2]:


x = "Hello World"	# str
print(type(x))


# In[3]:


x = 20	# int
print(type(x))


# In[4]:


x = 20.5	# float
print(type(x))


# In[5]:


x = 1j	# complex
print(type(x))


# In[6]:


x = ["apple", "banana", "cherry"]	# list
print(type(x))


# In[7]:


x = ("apple", "banana", "cherry")	# tuple
print(type(x))


# In[8]:


x = range(6)	# range
print(type(x))


# In[9]:


x = {"name" : "John", "age" : 36}	# dict
print(type(x))


# In[10]:


x = {"apple", "banana", "cherry"}	# set
print(type(x))


# In[11]:


x = frozenset({"apple", "banana", "cherry"})	# frozenset
print(type(x))


# In[12]:


x = True	# bool
print(type(x))


# In[13]:


x = b"Hello"	# bytes
print(type(x))


# In[14]:


x = bytearray(5)	# bytearray
print(type(x))


# In[15]:


x = memoryview(bytes(5))	# memoryview
print(type(x))


# ## Specifying a Particular Data Type
# The following function Object() { [native code] } functions can be used to indicate the data type:

# In[16]:


x = str("Hello World")	# str
print(type(x))


# In[17]:


x = int(20)	# int
print(type(x))


# In[18]:


x = float(20.5)	# float
print(type(x))


# In[19]:


x = complex(1j)	# complex
print(type(x))


# In[20]:


x = list(("apple", "banana", "cherry"))	# list
print(type(x))


# In[21]:


x = tuple(("apple", "banana", "cherry"))	# tuple
print(type(x))


# In[22]:


x = range(6)	# range
print(type(x))


# In[23]:


x = dict(name="John", age=36)	# dict
print(type(x))


# In[24]:


x = set(("apple", "banana", "cherry"))	# set
print(type(x))


# In[25]:


x = frozenset(("apple", "banana", "cherry"))	# frozenset
print(type(x))


# In[26]:


x = bool(5)	# bool
print(type(x))


# In[27]:


x = bytes(5)	# bytes
print(type(x))


# In[28]:


x = bytearray(5)	# bytearray
print(type(x))


# In[29]:


x = memoryview(bytes(5))	# memoryview
print(type(x))

