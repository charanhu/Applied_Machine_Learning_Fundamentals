#!/usr/bin/env python
# coding: utf-8

# # Python Syntax

# Python syntax is very simple and easy to learn. It is very similar to the English language.
# It can be executed in two ways:
# 1. Interactive Mode
# 2. Script Mode

# ### Interactive Mode
# In interactive mode, you can type Python statements directly in the terminal and the interpreter will execute them immediately.
# To start the interactive mode, type python in the terminal.
# The following is the output of the interactive mode:
# 
#     Python 3.6.5 (default, Apr 1 2018, 05:46:30)
#     [GCC 7.3.0] on linux
# 
# Example:
# 
#     >>> 1 + 1
#     2
# 
#     >>> print("Hello World")
#     Hello World

# ### Script Mode
# In script mode, you can write Python statements in a file and then execute the file. 
# To start the script mode, type python followed by the file name in the terminal. 
# The following is the output of the script mode:
# 
#     $ python hello.py
#     Hello World

# ## Python Indentation

# Python uses indentation to indicate a block of code.
# 
# Python will give you an error if you skip the indentation:

# In[1]:


# Example: Python Indentation

if 5 > 2:
print("Five is greater than two!")
# Python will give you an error if you skip the indentation:


# The number of spaces is up to you as a programmer, but it has to be at least one.

# In[2]:


# Example: Python Indentation
if 5 > 2:
 print("Five is greater than two!")

# Example: Python Indentation
if 5 > 2:
    print("Five is greater than two!")


# The spaces must be the same size in the same block of code, otherwise Python will give you an error.

# In[3]:


# Example: Python Indentation
if 5 > 2:
    print("Five is greater than two!")
        print("Five is greater than two!")

