
# coding: utf-8

# In[17]:

import csv                                #Importing all required packages
import pandas as pd
import numpy as np
from pandas import DataFrame


# In[18]:

file = pd.read_csv('C://Users//Pratik//Desktop//Data for Assignment 3//employee_compensation.csv')     #Fetching data from employee_compensation csv file into file      
df = DataFrame(file)
df


# In[19]:

#Calculating average compensation of different departments in an organization
df1 = df.groupby(['Organization Group', 'Department'])['Total Compensation'].mean().reset_index().sort_values(["Organization Group","Total Compensation"],ascending=[True,False]) 
df1.set_index('Organization Group',inplace = True)

#Sorting the total compensation in descending order
df2 = df1.sort_values(['Total Compensation'], ascending = [False])

#Displaying the top 30 results
df2.head(30)


# In[20]:

df2.to_csv('Question-2_Part-1.csv')


# In[ ]:



