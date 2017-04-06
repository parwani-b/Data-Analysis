
# coding: utf-8

# In[19]:

import csv
import pandas as pd
import numpy as np
from pandas import DataFrame
import datetime
import calendar


# In[20]:

file = pd.read_csv('C://Users//Pratik//Desktop//Data for Assignment 3//movies_awards.csv')


# In[21]:

df= DataFrame(file, columns = ['Awards'])
df = df.dropna() 
df['Awards_won']= df['Awards'].str.extract('(\d+) win',expand = True)
df['Awards_nominated']  = df['Awards'].str.extract('(\d+) nomination',expand = True)
df['Prime_Awards_won']  = df['Awards'].str.extract('Won (\d+) Primetime',expand = True)
df['Prime_Awards_nominated'] = df['Awards'].str.extract('Nominated for (\d+) PrimeTime',expand = True)
df['Bafta_Awards_won']  = df['Awards'].str.extract('Won (\d+) BAFTA',expand = True)
df['Bafta_Awards_nominated'] = df['Awards'].str.extract('Nominated for (\d+) BAFTA',expand = True)
df['Oscar_Awards_won']  = df['Awards'].str.extract('Won (\d+) Oscar',expand = True)
df['Oscar_Awards_nominated'] = df['Awards'].str.extract('Nominated for (\d+) Oscar',expand = True)
df['GoldenGlobe_Awards_won']  = df['Awards'].str.extract('Won (\d+) Golden Globe',expand = True)
df['GoldenGlobe_Awards_nominated'] = df['Awards'].str.extract('Nominated for (\d+) Golden Globe',expand = True)


# In[18]:

df = df.fillna(0)
df


# In[11]:

df['Awards_won'] = df['Awards_won'].astype(str).astype(int)
df['Awards_nominated'] =df['Awards_nominated'].astype(str).astype(int) 
df['Prime_Awards_won'] = df['Prime_Awards_won'].astype(str).astype(int)
df['Prime_Awards_nominated']=df['Prime_Awards_nominated'].astype(str).astype(int)
df['Bafta_Awards_won']=df['Bafta_Awards_won'].astype(str).astype(int) 
df['Bafta_Awards_nominated']=df['Bafta_Awards_nominated'].astype(str).astype(int)
df['Oscar_Awards_won']=df['Oscar_Awards_won'].astype(str).astype(int) 
df['Oscar_Awards_nominated']=df['Oscar_Awards_nominated'].astype(str).astype(int)
df['GoldenGlobe_Awards_won']=df['GoldenGlobe_Awards_won'].astype(str).astype(int)
df['GoldenGlobe_Awards_nominated']=df['GoldenGlobe_Awards_nominated'].astype(str).astype(int)


# In[22]:

df['Awards_won'] = df['Awards_won']+df['Prime_Awards_won']+df['Bafta_Awards_won']+df['Oscar_Awards_won']+df['GoldenGlobe_Awards_won']
df['Awards_nominated']=df['Awards_nominated']+df['Prime_Awards_nominated']+df['Bafta_Awards_nominated']+df['Oscar_Awards_nominated']+df['GoldenGlobe_Awards_nominated']


# In[23]:

print(df.head())


# In[24]:

df.to_csv('Question-4_Part-1.csv')


# In[ ]:



