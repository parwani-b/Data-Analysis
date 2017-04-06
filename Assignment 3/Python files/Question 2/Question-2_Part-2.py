
# coding: utf-8

# In[9]:

import csv                              #Importing all required packages
import pandas as pd
import numpy as np
from pandas import DataFrame


# In[10]:

file = pd.read_csv('C://Users//Pratik//Desktop//Data for Assignment 3//employee_compensation.csv')     #Fetching data from employee_compensation csv file into file      
df = DataFrame(file)
df


# In[11]:

df1 = DataFrame(file)               #Creating new dataframe
df1['Employee Identifier'] = df1['Employee Identifier'].where(df1['Overtime']>((5/100)*df1['Salaries']))   #Fetching employees whose overtime salary is greater than 5% of salaries
df1 = df1.dropna()      #Elimating all the NaN values from the fetched data


# In[12]:

#Creating a new empty dataframe
df_new = DataFrame()  
#Calculating average benefits for Job Family
df_new['Total Benefits'] = df1.groupby(['Job Family'])['Total Benefits'].mean() 
#Calculating average compensation for Job Family
df_new['Total Compensation'] = df1.groupby(['Job Family'])['Total Compensation'].mean()
#Calculating percntage of total benefits over total compensation for Job Family
df_new['Percentage Total Benefits'] = (df_new['Total Benefits']/df_new['Total Compensation']) * 100
#Displaying top 5 Job Families for highest percent of total benefits
df_new.sort_values('Percentage Total Benefits',ascending = False)[0:5]


# In[15]:

print(df_new.head())


# In[16]:

df_new.to_csv('Question-2_Part-2.csv')


# In[ ]:



