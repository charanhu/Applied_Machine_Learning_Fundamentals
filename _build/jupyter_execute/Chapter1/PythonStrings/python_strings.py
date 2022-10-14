#!/usr/bin/env python
# coding: utf-8

# # Python Strings
# Defination: A string is a sequence of characters. Strings are immutable. Strings are enclosed in single quotes or double quotes.

# ## Creating a string
# We can create a string by enclosing characters in quotes. Python treats single quotes the same as double quotes.

# In[1]:


# Example 1
str1 = 'Hello World'
print(str1)


# ## Assigning a string
# Defination: Assigning a string to a variable is called string assignment.

# In[2]:


# Example 2
str2 = "Hello World"
print(str2)


# ## Multiline Strings
# Defination: We can assign a multiline string to a variable by using three quotes.

# In[3]:


# Example 3
str3 = """Hello World
This is a multiline string"""
print(str3)


# In[4]:


# Example 4: using single quotes
str4 = '''Hello World
This is a multiline string'''
print(str4)


# ## Slice Strings
# Defination: We can access substrings, by using the slice syntax.
# 
# Slicing of strings is done by using the slice operator ( [ ] and [ : ] ) with indexes starting at 0 in the beginning of the string and working their way from -1 at the end.

# In[5]:


#Example 5
str5 = "Hello World"
print(str5[0:5])


# ## Slice from the start
# Defination: By leaving out the start index, the range will start at the first character.

# In[6]:


# Example 6
str6 = "Hello World"
print(str6[:5])


# ## Slice to the end
# Defination: By leaving out the end index, the range will go to the end.

# In[7]:


# Example 7
str7 = "Hello World"
print(str7[6:])


# ## Negative Indexing
# Defination: Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.

# In[8]:


# Example 8
str8 = "Hello World"
print(str8[-5:-2])


# ## Modify Strings
# Defination: We cannot change the value of a string. We can only assign a new string to the same name.

# In[9]:


# Example 9
str9 = "Hello World"
str9[0] = 'J'
print(str9)


# ## String Upper Case
# Defination: We can convert a string into upper case by using upper() method.
# 
# Syntax of upper() method with parameters: string.upper()

# In[19]:


# Example 10
str10 = "Hello World"
print(str10.upper())


# ## String Lower Case
# Defination: We can convert a string into lower case by using lower() method.
# 
# Syntax of lower() method with parameters: string.lower()

# In[20]:


# Example 11
str11 = "Hello World"
print(str11.lower())


# ## String Replace
# Defination: We can replace a string with another string by using replace() method.
# 
# Syntax of replace() method with parameters: string.replace(old, new)
# 
# Parameters: 
# 1. old: old substring to be replaced.
# 2. new: new substring to be replaced.

# In[21]:


# Example 12
str12 = "Hello World"
print(str12.replace("H", "J"))


# ## String Remove Whitespace
# Defination: We can remove whitespace from the beginning or the end of a string by using strip() method.
# 
# Syntax of strip() method with parameters: string.strip()

# In[22]:


# Example 13
str13 = " Hello World "
print(str13.strip())


# ## String Split
# Defination: We can split a string into substrings by using split() method.
# 
# Syntax of split() method with parameters: string.split(separator, maxsplit)
# 
# Parameters:
# 1. separator: The is a delimiter. The string splits at this specified separator. If is not specified, any whitespace (space, newline etc.) string is a separator.
# 2. maxsplit: It is a number, which tells us to split the string into maximum of provided number of times. If it is not provided then there is no limit.

# In[23]:


# Example 14
str14 = "Hello World"
print(str14.split(" "))


# ## String Concatenation
# Defination: We can concatenate strings by using + operator.

# In[24]:


# Example 15
str15 = "Hello"
str16 = "World"
str17 = str15 + str16
print(str17)


# ## String Format
# Defination: We can format strings by using format() method.
# 
# Syntax of format() method with parameters: string.format(value1, value2, ...)

# In[25]:


# Example 16
str18 = "Hello"
str19 = "{} World"
print(str19.format(str18))


# ### String Format with Position
# Defination: We can format strings by using format() method with position. The position is the index of the argument in the format() method. The index starts from 0.

# In[26]:


# Example 17
str20 = "Hello"
str21 = "Charan"
str22 = "{0} this is {1}"
print(str22.format(str20, str21))


# ### String Format with Keyword
# Defination: We can format strings by using format() method with keyword.

# In[27]:


# Example 18
str23 = "Hello"
str24 = "Charan"
str25 = "{greeting} this is {name}"
print(str25.format(greeting = str23, name = str24))


# ### String Format with Variable
# Defination: We can format strings by using format() method with variable.

# In[28]:


# Example 19
str26 = "Hello"
str27 = "Charan"
str28 = "{greeting} this is {name}"
print(str28.format(greeting = str26, name = str27))


# ## String Escape Character
# Defination: We can use escape character to insert characters that are illegal in a string.

# In[29]:


# Example 20
str29 = "My name is \"Charan\""
print(str29)


# ## Escape Character:
# 1. \'	Single Quote
# 2. \\	Backslash
# 3. \n	New Line
# 4. \r	Carriage Return
# 5. \t	Tab
# 6. \b	Backspace
# 7. \f	Form Feed
# 8. \ooo	Octal value
# 9. \xhh	Hex value
