#!/usr/bin/env python
# coding: utf-8

# # Python Numbers

# Python numbers data type are 3 types:
# 1. int
# 2. float
# 3. complex

# ## Int
# int is a whole number, positive or negative, without decimals, of unlimited length.

# In[1]:


# Example:
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))


# ## Float
# float, or "floating point number" is a number, positive or negative, containing one or more decimals.

# In[2]:


# Example:
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))


# float can also be scientific numbers with an "e" to indicate the power of 10.

# In[3]:


# Example:
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))


# ## Complex
# complex numbers are written with a "j" as the imaginary part.

# In[4]:


# Example:
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))


# ## Type Conversion
# Python Numbers data type can be converted into another data type.

# In[5]:


# Example:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# convert from int to float:
a = float(x)
print("Type of  a is: ", type(a))

# bconvert from float to int:
b = int(y)
print("Type of  b is: ", type(b))

# convert from int to complex:
c = complex(x)
print("Type of  c is: ", type(c))


# ## Random Number
# Defination: Random number is a number, which can not be predicted logically.
# 
# Python random module can be used to generate random numbers.

# In[6]:


# Example:
import random
print(random.randrange(1, 10))

