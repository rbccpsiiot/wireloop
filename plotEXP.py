import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import sys



plt.rcParams["figure.figsize"]=[20,15]

#matplotlib.use('tkagg')
id=sys.argv[1]



user_dir = "users/"+str(id)

try:
	try:
		gsr=pd.read_csv(user_dir+"/gsr_readings.csv.filtered")
	except Exception as e:
		print("NOT FOUND: gsr_readings.csv.filtered")
		print("PLOTTING: gsr_readings.csv")
		gsr=pd.read_csv(user_dir+"/gsr_readings.csv")

	try:
		eve=pd.read_csv(user_dir+"/events.csv")
	except:
		print("No events found!")
except:
	print("User data not found!")
	sys.exit(1)



gsr.timestamp=pd.to_datetime(gsr.timestamp)
try:
	eve.timestamp=pd.to_datetime(eve.timestamp)
except:
	print()
avgvoltage=gsr["voltage"].mean()
ax=gsr.plot(x="timestamp", y="voltage", color='orange')
ax.set_ylim(avgvoltage-0.2, avgvoltage+0.2)
#ax=plt.plot(gsr.timestamp, gsr.voltage, color='orange')

ax2=ax.twinx()
try:
	ax2.stem(eve.timestamp, eve.event, 'b', basefmt="g")
except:
	print()

plt.savefig("{}/result.png".format(user_dir))
plt.show()


#-----------------auto-scaleplot-------------

avgvoltage=gsr["voltage"].mean()
ax=gsr.plot(x="timestamp", y="voltage", color='orange')
#ax.set_ylim(avgvoltage-0.2, avgvoltage+0.2)
#ax=plt.plot(gsr.timestamp, gsr.voltage, color='orange')

ax2=ax.twinx()
try:
	ax2.stem(eve.timestamp, eve.event, 'b', basefmt="g")
except:
	print()
plt.savefig("{}/result_autoscaled.png".format(user_dir))
plt.show()



#import os
#os.system("xdg-open {}/result.png".format(user_dir) )

