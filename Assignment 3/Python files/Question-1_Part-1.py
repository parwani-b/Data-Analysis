
# coding: utf-8

# In[16]:

import csv                                  #Importing all required packages 
import pandas as pd
import numpy as np
from pandas import DataFrame
import datetime
import calendar


# In[17]:

# with open('C://Users//Pratik//Desktop//Data for Assignment 3//vehicle_collisions.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter = ',')
#     for row in readCSV:
#         print(row)
file = pd.read_csv('C://Users//Pratik//Desktop//Data for Assignment 3//vehicle_collisions.csv')
df = DataFrame(file)
df['DATE'] = pd.to_datetime(file['DATE'])
df1 = df[(df['DATE'] > '2015-12-31') & (df['DATE'] < '2017-01-01')]
df1['MONTH'] = df['DATE'].dt.month
df1


# In[18]:

df = pd.read_csv('C://Users//Pratik//Desktop//Data for Assignment 3//vehicle_collisions.csv')


# In[19]:

df2 = DataFrame(columns = ['Manhattan','NYC','Percentage of Collsions'])
df2['Manhattan'] = df1[df1['BOROUGH']=='MANHATTAN'].groupby(['MONTH'],sort = False)['UNIQUE KEY'].count()
df2['NYC']=df1.groupby(['MONTH'])['UNIQUE KEY'].count()
df2['Percentage of Collsions']= (df2['Manhattan']/df2['NYC'])
df2


# In[20]:

df2.to_csv('Question-1_Part-1.csv')


# In[ ]:



