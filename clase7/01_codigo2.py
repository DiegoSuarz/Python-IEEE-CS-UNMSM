#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


#Creando mi DataSeries
s1 = pd.Series(["Marcos","Susana","Luis","Magaly"])
s1


# In[3]:


#Convertir Dataseries a DataFrame
df = s1.to_frame()
df


# In[4]:


#colocando un nombre a la cabecera del DataFrame:
df.rename(columns={0: "nombres"}, inplace= True) #inplace permite mantener el nombre de las cabeceras en las siguientes ejecuciones
df


# In[7]:


#Cambiar el nombre de las filas del DataFrame:
df.rename(index={0: "Empleado1",1: "Empleado2"},inplace= True)
df #imprimiendo el DataFrame


# In[8]:


#Reemplazar todos los datos de la primera columna
#df[0] = "María" #cambia a todos los emelentos de la columna 0 con "maria"


# In[9]:


df


# In[ ]:




