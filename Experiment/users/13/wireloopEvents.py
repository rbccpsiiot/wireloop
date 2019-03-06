import RPi.GPIO as GPIO
import time, datetime
import json
import sys
import os
import pandas as pd
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24,GPIO.IN)

data=[]

def send_stop():
#	global data
	row={'timestamp':'none','event':0}
	time.sleep(1)
	ts=time.time()
        st=datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%dT%H:%M:%S.%f")
        row['timestamp']=st
        row['event']=2
	data.append(row)
	print(row)
	df=pd.DataFrame(data)
	df['timestamp']=pd.to_datetime(df['timestamp'])
	df.to_csv('events.csv')
	#for row in data:
	#	line=str(row)
	#	#print(line)
	#	os.system('echo %s >> events.csv' %(line))
	#print("_____________________________"*4)
	#print(data)
	sys.exit(0)


def send_touch():
	row={'timestamp':'none','event':0}
	ts=time.time()
        st=datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%dT%H:%M:%S.%f")
        row['timestamp']=st
        row['event']=1
        data.append(row)
        print(row)


if __name__=='__main__':
#	global data
	IN_PIN=23
	STOP_PIN=24
	row={'timestamp':'none','event':0}
	ts=time.time()
	st=datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%dT%H:%M:%S.%f")
        row['timestamp']=st
        row['event']=0
        data.append(row)
	os.system('rm events.csv 2> /dev/null')
	print(row)
	while True:
		EVENT=GPIO.input(IN_PIN)
		STOP=GPIO.input(STOP_PIN)
		if EVENT:
			send_touch()
			time.sleep(.5)
		if STOP:
			send_stop()

