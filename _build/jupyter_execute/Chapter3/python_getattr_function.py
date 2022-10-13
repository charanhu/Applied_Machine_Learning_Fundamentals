#!/usr/bin/env python
# coding: utf-8

# # Python getattr() Function

# Python getattr() Function: The getattr() function returns the value of the specified attribute (property or method) from the specified object.
# 
# If the specified attribute does not exist, default value is returned.

# Syntax: getattr(object, attribute, default)
# 
# Parameters:
# 1. object: object whose attribute is to be returned
# 2. attribute: attribute name whose value is to be returned
# 3. default: default value to be returned if the attribute does not exist
# 
# Return Value: value of the specified attribute

# In[1]:


# Example 1: getattr() function
class Person:
    def __init__(self, age):
        self.age = age

# create a Person object with age 36
person = Person(36)

# get the value of the attribute which is defined in the class, i.e. age
print('The age of Person ',getattr(person, 'age', 40))


# In[2]:


# get the value of the attribute which is not defined in the class, i.e. name
print('The name of Person ',getattr(person, 'name', 'Unknown'))

