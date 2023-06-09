#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install apyori')


# In[4]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[24]:


dataset = pd.read_csv('Netflix.csv', header = None, encoding='latin-1') 
transactions = []
for i in range(0, 7466):
    transactions.append([str(dataset.values[i, j]) for j in range(0, 20)])


# In[51]:


from apyori import apriori

rules = apriori (transactions = transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)


# In[52]:


results = list(rules)
results


# In[56]:


def inspect(results):
    movie_1 = [tuple(result[2][0][0])[0] for result in results] 
    movie_2 = [tuple(result[2][0][1])[0] for result in results]
    supports = [result[1] for result in results]
    return list(zip(movie_1, movie_2, supports))
resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['Movie 1', 'Movie 2', 'Support'])


# In[63]:


resultsinDataFrame


# In[64]:


resultsinDataFrame.nlargest (n = 159, columns= 'Support')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




