#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[5]:


x = np.arange(0, 3 * np.pi, 0.2)
y = np.sin(x) #funcion seno
print("Estos son los valores de X \n")
print(x)
print()
print("Estos son los valores de Y \n")
print(y)


# In[6]:


plt.plot(x,y)
plt.show()


# In[7]:


#Graficar arreglo 

arreglo = np.array([(5,6,7),(9,5,6)])
print(arreglo)
arreglo2 = np.array([(2,3,4),(8,6,5)])
print(arreglo2)


# In[8]:


# funcion coseno en arreglo
y= np.cos(arreglo)
print(y)


# In[9]:


#Graficar 
plt.plot(arreglo,y)
plt.show()


# In[14]:


# Input:
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
species = np.genfromtxt(url, delimiter=',', dtype='str', usecols=4)
np.random.seed(100)
species_small = np.sort(np.random.choice(species, size=20))
species_small


# In[19]:


length = 14
start = 4
step = 4

def seq(start, length, step):
    end = start + (step*length)
    return np.arange(start, end, step)

seq(start, length, step)


# In[ ]:




