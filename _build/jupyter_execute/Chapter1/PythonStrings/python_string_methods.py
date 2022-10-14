#!/usr/bin/env python
# coding: utf-8

# # Python String Methods

# ## capitalize()
# Defination: The capitalize() method returns a copy of the string with only its first character capitalized.
# 
# Syntax of capitalize() method with Parameters: string.capitalize()

# In[1]:


# Example 1:
# Python program to demonstrate working of capitalize()
str1 = "python is awesome"
print("Old String: ", str1)
print("New String: ", str1.capitalize())


# ## casefold()
# Defination: The casefold() method is removes all case distinctions present in a string. It is used for caseless matching, i.e. ignores cases when comparing.
# 
# Syntax of casefold() method with Parameters: string.casefold()

# In[2]:


# Example 2:
# Python program to demonstrate working of casefold()
str2 = "PYTHON IS AWESOME"
print("Old String: ", str2)
print("New String: ", str2.casefold())


# ## center()
# Defination: The center() method returns a centered string of length width. Padding is done using the specified fillchar (default is a space).
# 
# Syntax of center() method with Parameters: string.center(width, fillchar)
# 
# Parameters:
# 1. width: This is the total width of the string.
# 2. fillchar: This is the character to be filled in the empty space.

# In[3]:


# Example 3:
# Python program to demonstrate working of center()
str3 = "python is awesome"
print("Old String: ", str3)
print("New String: ", str3.center(24, '*')) # 24 is the width of the string
# Output:
# Old String: python is awesome
# New String: ****python is awesome****


# ## count()
# Defination: The count() method returns the number of occurrences of a substring in the given string.
# 
# Syntax of count() method with Parameters: string.count(substring, start, end)
# 
# Parameters:
# 1. substring: This is the substring to be searched in the string.
# 2. start: This is the starting index within the string where search starts.
# 3. end: This is the ending index within the string where search ends.

# In[4]:


# Example 4:
# Python program to demonstrate working of count()
str4 = "python is awesome, is isn't it?"
print("Old String: ", str4)
print("Result: ", str4.count("is"))


# ## encode()
# Defination: The encode() method returns an encoded version of the given string. Default encoding is the current default string encoding.
# 
# Syntax of encode() method with Parameters: string.encode(encoding, errors)
# 
# Parameters:
# 1. encoding: This is the encoding type to be used to encode the string.
# 2. errors: This is the response when the encoding error occurs.

# In[5]:


# Example 5:
# Python program to demonstrate working of default encode()
str5 = "python is awesome"
print("Old String: ", str5)
print("Encoded String: ", str5.encode())


# In[6]:


# Example 6:
# Python program to demonstrate working of encode() with errors
str6 = "python is awesome"
print("Old String: ", str6)
print("Encoded String: ", str6.encode(encoding = 'ascii', errors = 'ignore'))


# ## endswith()
# Defination: The endswith() method returns True if a string ends with the specified suffix. If not, it returns False.
# 
# Syntax of endswith() method with Parameters: string.endswith(suffix, start, end)
# 
# Parameters:
# 1. suffix: This is the suffix to be searched in the string.
# 2. start: This is the starting index within the string where search starts.
# 3. end: This is the ending index within the string where search ends.

# In[7]:


# Example 7:
# Python program to demonstrate working of endswith()
str7 = "My name is Charan H U"
print("Old String: ", str7)
print("Result: ", str7.endswith("U"))


# ## expandtabs()
# Defination: The expandtabs() method returns a copy of the string where all tab characters are replaced with whitespace characters until the next multiple of tabsize parameter.
# 
# Syntax of expandtabs() method with Parameters: string.expandtabs(tabsize)
# 
# Parameters:
# 1. tabsize: This is the tab size to be used to replace the tab character.

# In[8]:


# Example 8:
# Python program to demonstrate working of expandtabs()
str8 = "My name is\tCharan H U"
print("Old String: ", str8)
print("New String: ", str8.expandtabs(16))


# ## find()
# Defination: The find() method returns the lowest index of the substring if it is found in given string. If its is not found then it returns -1.
# 
# Syntax of find() method with Parameters: string.find(substring, start, end)
# 
# Parameters:
# 1. substring: This is the substring to be searched in the string.
# 2. start: This is the starting index within the string where search starts.
# 3. end: This is the ending index within the string where search ends.

# In[9]:


# Example 9:
# Python program to demonstrate working of find()
str9 = "My name is Charan H U"
print("Old String: ", str9)
print("Result: ", str9.find("Charan"))


# In[10]:


# Example 10:
# Python program to demonstrate working of find() with start and end
str10 = "My name is Charan H U"
print("Old String: ", str10)
print("Result: ", str10.find("Charan", 10, 21))


# ## format()
# Defination: The format() method formats the specified value(s) and insert them inside the string's placeholder.
# 
# Syntax of format() method with Parameters: string.format(value1, value2, ...)
# 
# Parameters:
# 1. value1, value2, ...: These are the values to be inserted inside the string's placeholder.

# In[11]:


# Example 11:
# Python program to demonstrate working of format()
str11 = "My name is {}"
print("Old String: ", str11)
print("New String: ", str11.format("Charan H U"))


# ## format_map()
# Defination: The format_map() method formats the specified value(s) and insert them inside the string's placeholder.
# 
# Syntax of format_map() method with Parameters: string.format_map(mapping)
# 
# Parameters:
# 1. mapping: This is the mapping to be inserted inside the string's placeholder.

# In[12]:


# Example 12:
# Python program to demonstrate working of format_map()
str12 = "My name is {name}"
print("Old String: ", str12)
print("New String: ", str12.format_map({"name": "Charan H U"}))


# ## index()
# Defination: The index() method returns the lowest index of the substring if it is found in given string. If its is not found then it raises an exception.
# Syntax of index() method with Parameters: string.index(substring, start, end)
# Parameters:
# 1. substring: This is the substring to be searched in the string.
# 2. start: This is the starting index within the string where search starts.
# 3. end: This is the ending index within the string where search ends.

# In[13]:


# Example 13:
# Python program to demonstrate working of index()
str13 = "My name is Charan H U"
print("Old String: ", str13)
print("Result: ", str13.index("Charan"))


# In[14]:


# Example 14:
# Python program to demonstrate working of index() with start and end
str14 = "My name is Charan H U"
print("Old String: ", str14)
print("Result 1: ", str14.index("Charan", 10, 21))
print("Result 2: ", str14.index("Charan", 10, 15))


# ## isalnum()
# Defination: The isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False.
# 
# Syntax of isalnum() method with Parameters: string.isalnum()

# In[ ]:


# Example 15:
# Python program to demonstrate working of isalnum()
str15 = "My name is Charan H U"
str16 = "@@@$%^"
print("Old String 1: ", str15)
print("Result 1: ", str15.isalnum())
print("Old String 2: ", str16)
print("Result 2: ", str16.isalnum())


# ## isalpha()
# Defination: The isalpha() method returns True if all characters in the string are alphabets. If not, it returns False.
# 
# Syntax of isalpha() method with Parameters: string.isalpha()

# In[ ]:


# Example 16:
# Python program to demonstrate working of isalpha()
str17 = "My name is Charan H U"
str18 = "Charan"
print("Old String 1: ", str17)
print("Result 1: ", str17.isalpha())
print("Old String 2: ", str18)
print("Result 2: ", str18.isalpha())


# ## isdecimal()
# Defination: The isdecimal() method returns True if all characters in a string are decimal characters. If not, it returns False.
# 
# Syntax of isdecimal() method with Parameters: string.isdecimal()

# In[ ]:


# Example 17:
# Python program to demonstrate working of isdecimal()
str19 = "My name is Charan H U"
str20 = "1234567890"
print("Old String 1: ", str19)
print("Result 1: ", str19.isdecimal())
print("Old String 2: ", str20)
print("Result 2: ", str20.isdecimal())


# ## isdigit()
# Defination: The isdigit() method returns True if all characters in a string are digits. If not, it returns False.
# 
# Syntax of isdigit() method with Parameters: string.isdigit()

# In[ ]:


# Example 18:
# Python program to demonstrate working of isdigit()
str21 = "My name is Charan H U"
str22 = "1234567890"
print("Old String 1: ", str21)
print("Result 1: ", str21.isdigit())
print("Old String 2: ", str22)
print("Result 2: ", str22.isdigit())


# ## isidentifier()
# Defination: The isidentifier() method returns True if the string is a valid identifier in Python. If not, it returns False.
# 
# Syntax of isidentifier() method with Parameters: string.isidentifier()

# In[ ]:


# Example 19:
# Python program to demonstrate working of isidentifier()
str23 = "int"
str24 = "int1"
print("Old String 1: ", str23)
print("Result 1: ", str23.isidentifier())
print("Old String 2: ", str24)
print("Result 2: ", str24.isidentifier())


# ## islower()
# Defination: The islower() method returns True if all alphabets in a string are lowercase alphabets. If the string contains at least one uppercase alphabet, it returns False.
# 
# Syntax of islower() method with Parameters: string.islower()

# In[ ]:


# Example 20:
# Python program to demonstrate working of islower()
str25 = "My name is Charan H U"
str26 = "my name is charan h u"
print("Old String 1: ", str25)
print("Result 1: ", str25.islower())
print("Old String 2: ", str26)
print("Result 2: ", str26.islower())


# ## isnumeric()
# Defination: The isnumeric() method returns True if all characters in a string are numeric characters. If not, it returns False.
# 
# Syntax of isnumeric() method with Parameters: string.isnumeric()

# In[ ]:


# Example 21:
# Python program to demonstrate working of isnumeric()
str27 = "My name is Charan H U"
str28 = "1234567890"
print("Old String 1: ", str27)
print("Result 1: ", str27.isnumeric())
print("Old String 2: ", str28)
print("Result 2: ", str28.isnumeric())


# ## isprintable()
# Defination: The isprintable() method returns True if all characters in a string are printable or the string is empty. If not, it returns False.
# 
# Syntax of isprintable() method with Parameters: string.isprintable()

# In[ ]:


# Example 22:
# Python program to demonstrate working of isprintable()
str29 = "My name is Charan H U"
str30 = "My name is \nCharan H U #1?."
print("Old String 1: ", str29)
print("Result 1: ", str29.isprintable())
print("Old String 2: ", str30)
print("Result 2: ", str30.isprintable())


# ## isspace()
# Defination: The isspace() method returns True if there are only whitespace characters in the string. If not, it returns False.
# 
# Syntax of isspace() method with Parameters: string.isspace()

# In[ ]:


# Example 23:
# Python program to demonstrate working of isspace()
str31 = "My name is Charan H U"
str32 = " "
print("Old String 1: ", str31)
print("Result 1: ", str31.isspace())
print("Old String 2: ", str32)
print("Result 2: ", str32.isspace())


# ## istitle()
# Defination: The istitle() method returns True if the string follows the rules of a title. If not, it returns False.
# 
# rules of title() method
# 1. All words in a title start with a upper case letter
# 2. All other letters in a title are lower case
# 
# Syntax of istitle() method with Parameters: string.istitle()

# In[ ]:


# Example 24:
# Python program to demonstrate working of istitle()
str33 = "My name is Charan H U"
str34 = "My Name Is Charan H U"
print("Old String 1: ", str33)
print("Result 1: ", str33.istitle())
print("Old String 2: ", str34)
print("Result 2: ", str34.istitle())


# ## isupper()
# Defination: The isupper() method returns True if all alphabets in a string are uppercase alphabets. If the string contains at least one lowercase alphabet, it returns False.
# 
# Syntax of isupper() method with Parameters: string.isupper()

# In[ ]:


# Example 25:
# Python program to demonstrate working of isupper()
str35 = "My name is Charan H U"
str36 = "MY NAME IS CHARAN H U"
print("Old String 1: ", str35)
print("Result 1: ", str35.isupper())
print("Old String 2: ", str36)
print("Result 2: ", str36.isupper())


# ## join()
# Defination: The join() method returns a string concatenated with the elements of an iterable.
# 
# Syntax of join() method with Parameters: string.join(iterable)
# 
# Parameters:
# 1. iterable: iterable (list, tuple, string etc.) whose elements are to be joined.

# In[ ]:


# Example 26:
# Python program to demonstrate working of join()
str37 = "My name is"
str38 = " "
str39 = "Charan H U"
print("Result: ", str38.join((str37, str39)))


# ## ljust()
# Defination: The ljust() method returns a left-justified string of a given minimum width.
# 
# Syntax of ljust() method with Parameters: string.ljust(width, fillchar)
# 
# Parameters:
# 1. width: Minimum width of the string. If the width is less than the length of the string, the original string is returned.
# 2. fillchar (Optional): Fill character. Defaults to a space.
# 
# Note: The fillchar is added to the right of the string.

# In[ ]:


# Example 27:
# Python program to demonstrate working of ljust()
str40 = "My name is Charan H U"
print("Old String: ", str40)
print("Result String after ljust(30, '0'): ", str40.ljust(30, '0'))


# ## lower()
# Defination: The lower() method returns a copy of the string in which all case-based characters have been lowercased.
# 
# Syntax of lower() method with Parameters: string.lower()

# In[ ]:


# Example 28:
# Python program to demonstrate working of lower()
str41 = "My name is Charan H U"
print("Old String: ", str41)
print("Result String after lower(): ", str41.lower())


# ## lstrip()
# Defination: The lstrip() method returns a copy of the string with leading characters removed (based on the string argument passed).
# 
# Syntax of lstrip() method with Parameters: string.lstrip(chars)
# 
# Parameters:
# 1. chars (Optional): A set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a prefix; rather, all combinations of its values are stripped.

# In[ ]:


# Example 29:
# Python program to demonstrate working of lstrip()
str42 = "My name is Charan H U"
print("Old String: ", str42)
print("Result String after lstrip('My'): ", str42.lstrip('My'))


# ## maketrans()
# Defination: The maketrans() method returns a translation table to be used in translations.
# 
# Syntax of maketrans() method with Parameters: string.maketrans(x, y, z)
# 
# Parameters:
# 1. x: If only one argument is supplied, it must be a dictionary. Each key in the dictionary must be a single character string, and each value must also be a single character string.
# 2. y: If two arguments are passed, they must both be strings of equal length, and in the resulting dictionary, each character in x will be mapped to the character at the same position in y.
# 3. z: If there is a third argument, it must be a string, whose characters will be mapped to None in the result.

# In[ ]:


# Example 30:
# Python program to demonstrate working of maketrans()
str43 = "My name is Charan H U"
print("Old String: ", str43)
print("Result after maketrans(): ", str43.maketrans('My', 'Ch'))
print("Result after maketrans() using translate(): ", str43.translate(str43.maketrans('My', 'Ch')))


# ## partition()
# Defination: The partition() method splits the string at the first occurrence of argument string and returns a tuple containing the part before the separator, argument string and the part after the separator.
# 
# Syntax of partition() method with Parameters: string.partition(sep)
# 
# Parameters:
# 1. sep: The separator based on which to split the string. It defaults to any whitespace.

# In[ ]:


# Example 31:
# Python program to demonstrate working of partition()
str44 = "My name is Charan H U"
print("Old String: ", str44)
print("Result after partition('is'): ", str44.partition('is'))


# ## replace()
# Defination: The replace() method returns a copy of the string where all occurrences of a substring is replaced with another substring.
# 
# Syntax of replace() method with Parameters: string.replace(old, new, count)
# 
# Parameters:
# 1. old: This is old substring to be replaced.
# 2. new: This is new substring, which would replace old substring.
# 3. count (Optional): If this optional argument count is given, only the first count occurrences are replaced.

# In[ ]:


# Example 32:
# Python program to demonstrate working of replace()
str45 = "My name is Charan H U"
print("Old String: ", str45)
print("Result after replace('is', 'was'): ", str45.replace('is', 'was'))


# ## rfind()
# Defination: The rfind() method returns the last index where the substring str is found, or -1 if no such index exists, optionally restricting the search to string[beg:end].
# 
# Syntax of rfind() method with Parameters: string.rfind(str, beg=0, end=len(string))
# 
# Parameters:
# 1. str: This is the substring to be searched.
# 2. beg (Optional): This is the starting index, by default its 0.
# 3. end (Optional): This is the ending index, by default its equal to the length of the string.

# In[ ]:


# Example 33:
# Python program to demonstrate working of rfind()
str46 = "My name is Charan H U. This is My Book"
print("Old String: ", str46)
print("Result after rfind('is'): ", str46.rfind('is'))


# ## rindex()
# Defination: The rindex() method returns the last index where the substring str is found, or raises an exception if no such index exists, optionally restricting the search to string[beg:end].
# 
# Syntax of rindex() method with Parameters: string.rindex(str, beg=0, end=len(string))
# 
# Parameters:
# 1. str: This is the substring to be searched.
# 2. beg (Optional): This is the starting index, by default its 0.
# 3. end (Optional): This is the ending index, by default its equal to the length of the string.

# In[ ]:


# Example 34:
# Python program to demonstrate working of rindex()
str47 = "My name is Charan H U. This is My Book"
print("Old String: ", str47)
print("Result after rindex('is'): ", str47.rindex('is'))


# ## rjust()
# Defination: The rjust() method returns a right-justified string of a given minimum width.
# 
# Syntax of rjust() method with Parameters: string.rjust(width, fillchar)
# 
# Parameters:
# 1. width: This is the minimum width of the string. If the width is less than the length of the string, the string is returned unchanged.
# 2. fillchar (Optional): This is the filling character, default is a space.

# In[ ]:


# Example 35:
# Python program to demonstrate working of rjust()
str48 = "My name is Charan H U"
print("Old String: ", str48)
print("Result after rjust(30, '0'): ", str48.rjust(30, '0'))


# ## rpartition()
# Defination: The rpartition() method splits the string at the last occurrence of argument string and returns a tuple containing the part before the separator, argument string and the part after the separator.
# 
# Syntax of rpartition() method with Parameters: string.rpartition(sep)
# 
# Parameters:
# 1. sep: The separator based on which to split the string. It defaults to any whitespace.

# In[ ]:


# Example 36:
# Python program to demonstrate working of rpartition()
str49 = "My name is Charan H U. This is My Book"
print("Old String: ", str49)
print("Result after rpartition('is'): ", str49.rpartition('is'))


# ## rsplit()
# Defination: The rsplit() method splits a string from the right, returns a list.
# 
# Syntax of rsplit() method with Parameters: string.rsplit(sep=None, maxsplit=-1)
# 
# Parameters:
# 1. sep (Optional): The is a delimiter. The string splits at this specified separator. If is not provided then any white space is a separator.
# 2. maxsplit (Optional): The maxsplit defines the number of splits to do. Default value is -1, which is "all occurrences".

# In[ ]:


# Example 37:
# Python program to demonstrate working of rsplit()
str50 = "My name is Charan H U. This is My Book"
print("Old String: ", str50)
print("Result after rsplit('is'): ", str50.rsplit('is'))


# ## rstrip()
# Defination: The rstrip() method returns a copy of the string with trailing characters removed (based on the string argument passed).
# 
# Syntax of rstrip() method with Parameters: string.rstrip([chars])
# 
# Parameters:
# 1. chars (Optional): This is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a prefix or suffix; rather, all combinations of its values are stripped.
# 

# In[ ]:


# Example 38:
# Python program to demonstrate working of rstrip()
str51 = "My name is Charan H U. This is My Book"
print("Old String: ", str51)
print("Result after rstrip('is'): ", str51.rstrip('is'))


# ## split()
# Defination: The split() method splits a string into a list. You can specify the separator, default separator is any whitespace.
# 
# Syntax of split() method with Parameters: string.split(sep=None, maxsplit=-1)
# 
# Parameters:
# 1. sep (Optional): The is a delimiter. The string splits at this specified separator. If is not provided then any white space is a separator.
# 2. maxsplit (Optional): The maxsplit defines the number of splits to do. Default value is -1, which is "all occurrences".

# In[ ]:


# Example 39:
# Python program to demonstrate working of split()
str52 = "My name is Charan H U. This is My Book"
print("Old String: ", str52)
print("Result after split('is'): ", str52.split('is'))


# ## splitlines()
# Defination: The splitlines() method splits a string into a list. The splitting is done at line boundaries.
# 
# Syntax of splitlines() method with Parameters: string.splitlines([keepends])
# 
# Parameters:
# 1. keepends (Optional): This is a boolean value. If true, line breaks are also included in the resulting list.

# In[ ]:


# Example 40:
# Python program to demonstrate working of splitlines()
str53 = """My name is 
Charan H U. 
This is My Book"""
print("Old String: ", str53)
print("Result after splitlines(): ", str53.splitlines())


# ## startswith()
# Defination: The startswith() method returns true if a string starts with the specified prefix. If not, it returns false.
# 
# Syntax of startswith() method with Parameters: string.startswith(prefix, start, end)
# 
# Parameters:
# 1. prefix: This is the prefix to be checked.
# 2. start (Optional): This is the starting index within the string where prefix is to be checked.
# 3. end (Optional): This is the ending index within the string where prefix is to be checked.

# In[ ]:


# Example 41:
# Python program to demonstrate working of startswith()
str54 = "My name is Charan H U. This is My Book"
print("Old String: ", str54)
print("Result after startswith('My'): ", str54.startswith('My'))
print("Result after startswith('Charan'): ", str54.startswith('Charan'))


# ## strip()
# Defination: The strip() method returns a copy of the string with both leading and trailing characters removed (based on the string argument passed).
# 
# Syntax of strip() method with Parameters: string.strip([chars])
# 
# Parameters:
# 1. chars (Optional): This is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a prefix or suffix; rather, all combinations of its values are stripped.

# In[ ]:


# Example 42:
# Python program to demonstrate working of strip()
str55 = "               Charan H U               "
print("Old String: ", str55)
str56 = "My name is "+str55.strip()+" This is My Book"
print("New String: ", str56)


# ## swapcase()
# Defination: The swapcase() method returns a copy of the string with uppercase characters converted to lowercase and vice versa.
# 
# Syntax of swapcase() method with Parameters: string.swapcase()

# In[59]:


# Example 43:
# Python program to demonstrate working of swapcase()
str57 = "My name is Charan H U. This is My Book"
print("Old String: ", str57)
print("Result after swapcase(): ", str57.swapcase())


# ## title()
# Defination: The title() method returns a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.
# 
# Syntax of title() method with Parameters: string.title()

# In[60]:


# Example 44:
# Python program to demonstrate working of title()
str58 = "My name is Charan H U. This is My Book"
print("Old String: ", str58)
print("Result after title(): ", str58.title())


# ## translate()
# Defination: The translate() method returns a copy of the string in which each character has been mapped through the given translation table.
# 
# Syntax of translate() method with Parameters: string.translate(table, deletechars="")
# 
# Parameters:
# 1. table: This is the translation table to be used for translating the characters.
# 2. deletechars (Optional): This is a string containing the characters to be deleted.

# In[61]:


# Example 45:
# Python program to demonstrate working of translate()
str59 = "My name is Charan H U. This is My Book"
print("Old String: ", str59)
print("Result after translate(): ", str59.translate({ord('a'): 'b', ord('b'): 'a'}))


# ## upper()
# Defination: The upper() method returns a copy of the string converted to uppercase.
# 
# Syntax of upper() method with Parameters: string.upper()

# In[62]:


# Example 46:
# Python program to demonstrate working of upper()
str60 = "My name is Charan H U. This is My Book"
print("Old String: ", str60)
print("Result after upper(): ", str60.upper())


# ## zfill()
# Defination: The zfill() method returns a copy of the string with '0' characters padded to the left.
# 
# Syntax of zfill() method with Parameters: string.zfill(width)
# 
# Parameters:
# 1. width: This is the length of the string with the '0' characters padded to the left.

# In[63]:


# Example 47:
# Python program to demonstrate working of zfill()
str61 = "My name is Charan H U. This is My Book"
print("Old String: ", str61)
print("Result after zfill(50): ", str61.zfill(50))

