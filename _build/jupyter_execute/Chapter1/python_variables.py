#!/usr/bin/env python
# coding: utf-8

# # Python Variables

# Defination: A variable is a container for a value, which can be of various types.
# 
# A variable is created the moment you first assign a value to it.
# 
# Variable names are case-sensitive.
# 
# Variable names can be short (like x and y) or more descriptive (age, carname, total_volume).
# 
# ## Rules for Python variables:
# 1. A variable name must start with a letter or the underscore character
# 2. A variable name cannot start with a number
# 3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# 4. Variable names are case-sensitive (age, Age and AGE are three different variables)

# ## Creating Varibales

# Python has no command for declaring a variable.
# 
# A variable is created the moment you first assign a value to it.

# In[1]:


# Example
x = 4 # x is of type int
print(x)


# Python allows you to assign values to multiple variables in one line:

# In[2]:


# Example
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


# And you can assign the same value to multiple variables in one line:

# In[3]:


# Example
x = y = z = "Orange"
print(x)
print(y)
print(z)


# To combine both text and a variable, Python uses the + character:

# In[4]:


# Example
x = "awesome"
print("Python is " + x)


# You can also use the + character to add a variable to another variable:

# In[5]:


# Example
x = "Python is "
y = "awesome"
z =  x + y
print(z)


# For numbers, the + character works as a mathematical operator:

# In[6]:


# Example
x = 5
y = 10
print(x + y)


# If you try to combine a string and a number, Python will give you an error:

# In[7]:


# Example
x = 5
y = "John"
print(x + y)


# To add a space between them, add a " ":

# In[ ]:


# Example
x = 5
y = "John"
print(x + y)


# ## Casting
# If you want to specify the data type of a variable, this can be done with casting.

# In[ ]:


# Example
x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0


# ## Get the Type
# You can get the data type of a variable with the type() function.

# In[ ]:


# Example
x = 5
y = "John"
print(type(x))
print(type(y))


# ## Single or Double Quotes?
# String variables can be declared either by using single or double quotes:

# In[ ]:


# Example
x = "John"
# is the same as
x = 'John'


# ## Case-Sensitive
# Variable names are case-sensitive.

# In[ ]:


# Example
a = 4
A = "Sally"
#A will not overwrite a
print(a)
print(A)


# ## Legal variable names
# 1. myvar
# 2. my_var
# 3. _my_var
# 4. myVar
# 5. MYVAR
# 6. myvar2

# In[ ]:


# Legal variable names with examples
myvar = "Apple"
print(myvar)

my_var = "Apple"
print(my_var)

_my_var = "Apple"
print(_my_var)

myVar = "Apple"
print(myVar)

MYVAR = "Apple"
print(MYVAR)

myvar2 = "Apple"
print(myvar2)


# ## Illegal variable names
# 1. 2myvar
# 2. my-var
# 3. my var

# In[ ]:


# Illegal variable names with examples
2myvar = "Apple"
print(2myvar)


# In[ ]:


my-var = "Apple"
print(my-var)


# In[41]:


my var = "Apple"
print(my var)


# ## Unpacking a Collection
# Unpacking a collection of values into variables is called unpacking.

# In[42]:


# Example
animals = ["Dog", "Cat", "Bird"]
(x, y, z) = animals
print(x)
print(y)
print(z)


# ## Python Output Variables
# Defination: The Python print statement is often used to output variables.
# 
# Python uses the print statement to output data to the standard output device (screen).

# In[43]:


# Example:
x = "awesome"
print("Python is " + x)


# We can also output multiple variables at the same time

# In[45]:


# Example:
x = "Python is "
y = "awesome"
z =  x + y
print(x + y)


# ## Python Global Variables
# Defination: Variables that are created outside of a function (as in all of the examples above) are known as global variables.

# In[46]:


x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()


# Global variables can be used by everyone, both inside of functions and outside.

# In[47]:


# Example:
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)


# Defining a global variable inside a function is done by using the global keyword. 

# In[48]:


# Example:
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

