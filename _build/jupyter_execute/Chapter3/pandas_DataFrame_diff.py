#!/usr/bin/env python
# coding: utf-8

# # pandas.DataFrame.diff()

# pandas diff() is used to find the difference of a DataFrame element compared with another element in
# the DataFrame (default is element in the same column of the previous row).

# Syntax: DataFrame.diff(periods=1, axis=0)
# 
# Parameters:
# 
#     periods: int, default 1. Periods to shift for calculating difference, accepts negative values.
#     axis: {0 or ‘index’, 1 or ‘columns’}, default 0. Take difference over rows (0) or columns (1).
#     Returns: DataFrame or Series of the same size and shape as the input.

# In[1]:


# Example: diff
import pandas as pd

# Create a dataframe
df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6],
                     'B': [1, 1, 2, 3, 5, 8],
                        'C': [1, 4, 9, 16, 25, 36]})
print(df)


# Calculate the difference between the current and a shifted row.
# 
# The default is to shift by one row
# 
#     step by step:
#     1. current row: 2, 1, 4
#     2. shifted row: 1, 1, 1
#     3. difference: 1, 0, 3

# In[2]:


# Calculate the difference between the current and a shifted row

print(df.diff())


# Calculate the difference between the current and a shifted row of period 2.
# 
# period 2 means the difference between the current row and the row 2 rows before it.
# 
#     step by step:
#     1. current row: 6, 8, 36
#     2. shifted row: 4, 3, 16
#     3. difference: 2, 5, 20

# In[3]:


# Calculate the difference between the current and a shifted row of period 2

df.diff(periods=2)


# Calculate the difference between the current and a shifted row of axis 1.
# 
# axis=1 means column wise operation and axis=0 means row wise operation.
# 
#     step by step for axis 1 and period 2
#     1. current column: 1, 4, 9, 16, 25, 36
#     2. shifted column: 1, 2, 3, 4, 5, 6
#     3. difference: 0, 2, 6, 12, 20, 30

# In[4]:


# Calculate the difference between the current and a shifted row of axis 1 and period 2

df.diff(periods=2, axis=1)

