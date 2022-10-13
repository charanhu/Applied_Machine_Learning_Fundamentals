#!/usr/bin/env python
# coding: utf-8

# # Python getattr() Function

# In[1]:


# Python getattr() Function: The getattr() function returns the value of the
# specified attribute (property or method) from the specified object.
# If the specified attribute does not exist, default value is returned.

# Syntax: getattr(object, attribute, default)
# Parameters:
#               object: object whose attribute is to be returned
#               attribute: attribute name whose value is to be returned
#               default: default value to be returned if the attribute does not exist

# Return Value: value of the specified attribute


# In[2]:


# Example 1: getattr() function
class Person:
    def __init__(self, age):
        self.age = age

# create a Person object with age 36
person = Person(36)

# get the value of the attribute 'age'
print('The age of Person ',getattr(person, 'age', 40))

# get the value of the attribute 'salary'
print('The salary of Person ',getattr(person, 'salary', 10000))


# In[3]:


# Python getattr() Function for getting the value of a method or class attribute from an object or class respectively is shown in the following example.

