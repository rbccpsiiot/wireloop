#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd
import datetime
from datetime import timedelta
import sys
import matplotlib.pyplot as plt


# In[47]:


eve=pd.read_csv("events.csv")
eve.timestamp=pd.to_datetime(eve.timestamp)


# In[35]:


startt=pd.to_datetime(eve[eve.event==0]['timestamp'].tolist()[0])
stopt=pd.to_datetime(eve[eve.event==2]['timestamp'].tolist()[0])


# In[58]:


timetaken=stopt-startt


# In[59]:


timetaken=timetaken.seconds


# In[60]:


noOfTouches=eve[eve.event==1].shape[0]


# In[62]:


<<<<<<< HEAD
score=(timetaken+(noOfTouches)**2)*5
=======
score=timetaken+noOfTouches*5
>>>>>>> b35ef519d57715bf805a13bb8285ce6778e43c58
timetaken=str(datetime.timedelta(seconds=timetaken))


# In[64]:


print('Your score is:',score)
print('You took', timetaken, 'to complete.')
<<<<<<< HEAD
print('Number of touches:', noOfTouches)
=======

>>>>>>> b35ef519d57715bf805a13bb8285ce6778e43c58

# In[50]:


# plt.stem(eve.timestamp, eve.event)


# In[49]:


# %matplotlib


# In[ ]:




