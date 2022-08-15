#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import urllib.request as url2


# In[2]:


url = "https://datahub.smcgov.org/id/mb6a-xn89.json"

#conexion al archivo JSON:
response = url2.urlopen(url)

print(response)

head = ["geografía", "tipo_geografía", "tiempo"]


# In[3]:


df = pd.read_json(url)


# In[4]:


df.head()


# In[ ]:




