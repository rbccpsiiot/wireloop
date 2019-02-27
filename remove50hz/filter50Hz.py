#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


plt.rcParams['figure.figsize'] = [15, 5]


# In[4]:


import os

#os.environ["ISA_USER_ID"] = "1"

if not "ISA_USER_ID" in os.environ:
    print("PASS ENV VARIABLE ->  ISA_USER_ID")
    exit()
    
vizFlag=True
if "ISA_NO_PLOT" in os.environ:
    vizFlag = False
        
userid=os.environ["ISA_USER_ID"]


# In[5]:


#userid=1
filename="../users/{}/gsr_readings.csv".format(userid)


# In[6]:


gsr = pd.read_csv(filename)


# In[7]:


gsr.timestamp = pd.to_datetime(gsr.timestamp)


# In[8]:


if vizFlag:
    plt.plot(gsr.timestamp,gsr.voltage)


# In[9]:


if vizFlag:
    plt.plot(gsr.timestamp,gsr.voltage.diff() > 0.01)


# In[ ]:


threshold50Hz = 0.01

mask = (gsr.voltage.diff() > threshold50Hz)
mask[0] = False
nPeaks=mask.apply(lambda x: 1 if x else 0).sum()


# In[ ]:


df = gsr.voltage
normalized_df=(df-df.min())/(df.max()-df.min())
gsr["normalised_voltage"] = normalized_df


# In[ ]:


if vizFlag:
    plt.plot(gsr.timestamp.head(100),gsr.normalised_voltage.head(100))
    plt.stem(gsr[mask].timestamp.head(5),[1]*5,'r')


# In[11]:


for indx in gsr[mask].index:
    if indx == gsr.shape[0]-1:
        window_indices=[indx-2,indx-1]
    else:
        window_indices=[indx-1,indx+1]
        
    normalised_voltage_mean=gsr.iloc[window_indices].normalised_voltage.mean()
    voltage_mean=gsr.iloc[window_indices].voltage.mean()
    
    gsr.normalised_voltage.iloc[indx] = normalised_voltage_mean
    gsr.voltage.iloc[indx] = voltage_mean


# In[ ]:


if vizFlag:
    #plt.plot(gsr.timestamp,gsr.normalised_voltage)
    plt.plot(gsr.timestamp,gsr.voltage)
    #plt.stem(gsr[mask].timestamp,[1]*nPeaks,'r')


# In[ ]:


gsr.to_csv("{}.filtered".format(filename),index=False)


# In[ ]:




