#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#AGENDA:
    #1.extract the website using web scraping using python
    #2.use libraries of python to manipulate the dataset
    #3.feed the updated data in a data frame
    #4.come up with new data frame that differ the original
#GOAL:
    #use and test of python libraries and its efficiency to maximum with the scraping data


# In[5]:


#using request to get the url,beautifulsoup to get html code from url,pandas to create dataframe 
import numpy as np
import pandas as pd
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
DF=pd.DataFrame()


# In[11]:


url='https://www.myntra.com/?utm_source=vcommission&utm_medium=affiliate_102f90373c9af8783492f47238b312'
get_url = requests.get(url)
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
soup


# In[ ]:




