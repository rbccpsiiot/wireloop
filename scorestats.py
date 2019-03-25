

import os

users= sorted(os.listdir("users"),key=lambda x: int(x))
#print users


users=filter(lambda x: int(x)>39,users)

#print users

def getScore(line1,line2):
    score=int(line2.split(":")[-1].strip())
    name=line1.split(":")[0].strip()
    return {name:score}


scores=[]

for user in users:
    with open("users/%s/%s" % (user,user)) as g:
        userline = g.readline()
        scoreline = g.readline()
        try:
            score = getScore(userline,scoreline)
            scores.append(score)
        except:
            print("Exception in %s" % scoreline)

def leaderboard(scores):
    scores = sorted(scores,key=lambda x: x[list(x.keys())[0]] )
    print (scores)
    with open("leaderboard.txt",'w') as g:
        for s in scores:
            for name in s:
                g.write(name + " " * (20 - len(name)) + "%s\n" %s[name])
                #print (name)


#generate score
leaderboard(scores)

STATS={}

import numpy as np

allscores=[]
for x in scores:
    for y in x:
        allscores.append(x[y])

#print (allscores)

STATS["mean"] = np.mean(allscores)
#STATS["std"] = np.sqrt(np.sum((np.array(allscores) - STATS['mean']) **2)/len(allscores))
STATS['std']=np.std(allscores)

print("MEAN: %s \t STD: %s" % (STATS['mean'],STATS['std']))

#import seaborn as sns

#import matplotlib.pyplot as plt
#plt.barplot(allscores)
