
# coding: utf-8

# In[25]:

import pandas as pd              #Importing all required packages
import numpy as np
from pandas import DataFrame


# In[26]:

#Fetching data from cricket_matches csv file into file 
file = pd.read_csv('C://Users//Pratik//Desktop//Data for Assignment 3//cricket_matches.csv')  
df = DataFrame(file)                    
df


# In[27]:

#Creating new dataframe and fetching required columns
df1 = DataFrame(df, columns = ['home','winner','innings1_runs','innings2_runs','innings1','innings2','score','avg_score'])
df2 = DataFrame(columns = ['Average Score',])
#Fetching teams that hosted the game and were also winners
df1 = df1[df1['home']==(df1['winner'])]
# Fetching scores from columns innings1_runs or innings2_runs on the basis of winning
df1['score'] = df1['innings1_runs'].where(df1['home'] == df1['innings1'], df1['innings2_runs'])
#df1
#Calculating average score of each team
df2['Average Score'] = df1.groupby('home')['score'].mean()
#Displaying the result
df2


# In[28]:

df2.to_csv('Question-3_Part-1.csv')   #Converting the output to csv file


# In[ ]:



