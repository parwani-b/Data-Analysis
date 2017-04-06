
# coding: utf-8

# In[23]:

import pandas as pd                                #Importing all required packages
import numpy as np 
from pandas import Series, DataFrame


# In[24]:

file = pd.read_csv('C://Users//Pratik//Desktop//Data for Assignment 3//vehicle_collisions.csv')        #Fetching vehicle_collisions csv file into variable file 
df = DataFrame(file)                        


# In[26]:

df1 = df.groupby(['BOROUGH'],sort = False)['VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE'].count().reset_index()
df_new = DataFrame()                  #Creating a new empty dataframe


# In[27]:

df_new['BOROUGH'] = df1['BOROUGH']                   #Copying data of BOROUGH into new dataframe
df_new['ONE VEHICLE INVOLVED'] = df1['VEHICLE 1 TYPE'] - df1['VEHICLE 2 TYPE']    #Calculation of one vehicle involved
df_new['TWO VEHICLES INVOLVED'] = df1['VEHICLE 2 TYPE'] - df1['VEHICLE 3 TYPE']   #Calculation of two vehicle involved
df_new['THREE VEHICLES INVOLVED'] = df1['VEHICLE 3 TYPE'] - df1['VEHICLE 4 TYPE'] #Calculation of three vehicle involved
df_new['MORE VEHICLES INVOLVED'] = df1['VEHICLE 4 TYPE']             #Calculation of more vehicle involved
df_new.set_index('BOROUGH', inplace = True)
df_new


# In[28]:

df_new.to_csv('Question-1_Part-2.csv')


# In[ ]:



