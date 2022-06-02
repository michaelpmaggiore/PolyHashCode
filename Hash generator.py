#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import hashlib
import random


# In[2]:


a_string = 'poly'


# In[3]:


hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()
for i in range(14):
    n = random.random()
    hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()+f"{n}"
    hashed_string = hashlib.sha256(hashed_string.encode('utf-8')).hexdigest()
    
    print(hashed_string[-5:-1])
    time.sleep(4)


# In[ ]:




