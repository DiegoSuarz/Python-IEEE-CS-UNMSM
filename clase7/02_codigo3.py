#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json


# In[2]:


#Creando un Json Data
jsonData = '{"nombre": "python", "tipo":"Backend","Paradigma":"POO"}'
jsonData


# In[3]:


#convertir JSON a un valor Phyton (objeto) en un diccionario
dictionaryToJson = json.loads(jsonData)
dictionaryToJson


# In[ ]:




