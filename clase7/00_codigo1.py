#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd # as permite renombrar la libreria
import numpy as np


# In[3]:


series = pd.Series([100,np.NaN,500,1500])
series
#print(series) pycharm

# In[4]:


# fillna: reemplaza los valores non
series.fillna(0) #rellenar los datos NaN con 0


# In[5]:


#dropna no considera valores nan dentro de la salida de mi resultado 0
series.dropna()


# In[6]:


#is null muestra los datos que han cambiado de valor, los datos vacios o 0
series.isnull()


# In[ ]:




