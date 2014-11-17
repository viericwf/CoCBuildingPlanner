# coding: utf-8
buildings={'mortar':{'type':'gold',1:{'cost':1600000,'time':6},2:{'cost':3200000,'time':7}}}
buildings['cannon']={'type':'gold',1:{'cost':3200000,'time':5}}
worker=[0,0,0,0,0]
loot={'gold':0,'elixir':0,'dark_elixir':0}
earn={'gold':1500000,'elixir':500000,'dark_elixir':5000}
# earn per day
bound=0.1
# require per day <= (1+bound)*earn

now={'mortar':[0,0,0,0],'cannon':[0,0,0,0]}
obj={'mortar':[1,1,1,1],'cannon':[1,1,1,1]}
working={}

def getNextBuildings(now,working,obj):
    nextBuildings={}
    keys=now.keys()
    for k in working.keys():
        if k not in keys:
            keys.append(k)
            #keys denote all buildings including working ones
    for k in keys:
        total = now[k]
        print total
        total = [0]*len(keys)    
            
        for i in range(len(keys)):
            total[i]=max(now[keys][i],working[keys][i])
        if total is not obj[o]:
            levels=[]
            for i in range(len(now[o])):
                if total[i] is not obj[o][i]:
                    levels.append(total[i]+1)
            nextBuildings[o]=levels
    return nextBuildings
"""
def maxCollision = getMaxCollision(nextBuilding,earn):
 
def finish(now,working,obj):
    for o in obj:
        total = [0]*len(now[o])        
        for i in range(len(now[o])):
            total[i]=max(now[o][i],working[o][i])
        if total is not obj[o]:
            return False
    return True

def getTimeInterval(nextWorker):
    return nextWorker

def addLoot(loot,earn,timeInterval):
    for r in loot:
        newLoot{r}=loot[r]+earn*timeInterVal
    return newLoot

def addTime(time,timeInterval)
    return time+timeInterval

def updateWorker(worker,timeInterval)
    for w in worker:
        newWorker[w]=worker[w]+timeInterval
    return newWorker

def getMinInterval(nextBuilding,earn)
    interval={'gold':999,'elixir':999,'dark_elixir':999}
    for b in nextBuilding
        interval{r} = 
    maxInterval = gerMaxInterval(loot,earn)
    available = findAvailable(nextBuilding,loot,minInterval,maxIntervalmaxCollision)
    if available:
        if len(available) is 1:
            nextBuilding = available
        else
            nextBuilding = findBest(available,working,buildings)
    else:
        # no available building waiting resourse 
        # TBD
    worker = upWorker(worker,nextBuilding)
    working = upWorking(working, nextBuilding,worker)
    now = upNow(working,worker)
"""
nextBuildings = getNextBuildings(now,working,obj)
print 'nextBuildings: ',nextBuildings
maxCollision = getMaxCollision(nextBuilding,earn)
time = 0
while not finish(now,working,obj):
    sortedWorker = sorted(worker)
    nextWorker = sortedWorker[0]
    timeInterval = getTimeInterval(nextWorker)
    loot = addLoot(loot,earn,timeInterval)
    time = addTime(time,timeInterval)
    worker = updateWorker(worker,timeInterval)
    minInterval = getMinInterval(nextBuilding,earn)
    maxInterval = gerMaxInterval(loot,earn)
    available = findAvailable(nextBuilding,loot,minInterval,maxInterval,maxCollision)
    if available:
        if len(available) is 1:
            nextBuilding = available
        else:
            nextBuilding = findBest(available,working,buildings)
    else:
        print 'else'
        # no available building waiting resourse 
        # TBD
    worker = upWorker(worker,nextBuilding)
    working = upWorking(working, nextBuilding,worker)
    now = upNow(working,worker)
    earnPerDay=nextBuilding[2]/nextBuilding[3]
    print 'time: ',time,', Start build: ',nextBuilding[0],', require: ',nextBuilding[2],', require per day: ',earnPerDay

