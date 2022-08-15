#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_json("https://datahub.smcgov.org/id/mb6a-xn89.json")


# In[4]:


#Mostar los primeros 5 registros:
df.head(5)


# In[5]:


#devuelve la candidad de filas que exiten el el archivo json
df.shape[0]

#existen 32 filas


# In[6]:


df.describe()


# In[ ]:




