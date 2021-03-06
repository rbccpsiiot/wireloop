import pandas as pd
import time
import datetime
from datetime import timedelta

dat=pd.read_csv("data.dat")
dat['timestamp']=0
dat.columns=['voltage', 'timestamp']
#print(dat)
f=open('data_start_time.txt', 'r')
st=f.readline()
ts=pd.to_datetime(st)
dat.ix[0,'timestamp']=ts

for i, row in dat.iterrows():
	dat.ix[i,'timestamp']=ts + pd.to_timedelta(0.4*i, unit='s')
	#print(row['timestamp'])
dat.to_csv("gsr_readings.csv")

