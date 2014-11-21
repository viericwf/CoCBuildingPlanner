# coding: utf-8
import math
buildings={'mortar':{'type':'gold',1:{'cost':1600000,'time':6},2:{'cost':3200000,'time':7}}}
buildings['cannon']={'type':'gold',1:{'cost':3200000,'time':5}}
buildings['camp']={'type':'elixir',1:{'cost':2250000,'time':5}}

working=[('mortar',2,1),('camp',1,2),('mortar',2,3),('camp',1,4),('camp',1,5)]
#(n,l,t): upgrade n to l levels, time remain t
worker=[1,2,3,4,5]

loot={'gold':5000000,'elixir':0,'dark_elixir':0}
maxLoot={'gold':8001000,'elixir':8001000,'dark_elixir':80000}
earn={'gold':1500000,'elixir':500000,'dark_elixir':5000}
# earn per day
bound=0.1
# require per day <= (1+bound)*earn

now={'mortar':[1,1,1,0],'cannon':[0,0,0,0]}
obj={'mortar':[2,2,2,2],'cannon':[1,1,1,1]}
sortedWorker = sorted(worker)
nextWorker = sortedWorker[0]

def getNextBuildings(now,working,obj,nextWorker):
    """
    Parameters
    ==========

    Returns
    =======
    
    """
    nextBuildings=[]
    keys=now.keys()
    for k in working:
        if k[0] not in keys:
            keys.append(k)
            #keys denote all buildings including working ones
#    print 'keys: ',keys
    for k in keys:
        if now.has_key(k):
            total=now[k]
        for w in working:
            if w[0] is k:
                for i in range(len(total)):
                    if total[i] is w[1]-1 and w[2] is nextWorker:
                        total[i]=total[i]+1
                        break
#                    elif total[i] is w[1]-1:
#                        total[i]=total[i]+999
        if obj.has_key(k):
            if total is not obj[k]:
                objLevels=[]
                nowLevels=[]
                sortTotal=sorted(total,reverse=True)
                sortObj=sorted(obj[k],reverse=True)
#                print 'before: ',k,': nowLevels: ',sortTotal,' objLevels: ',sortObj
                for i in range(len(sortObj)):
                    if sortTotal[len(sortTotal)-1] is sortObj[len(sortObj)-1]:
                        sortTotal.pop()
                        sortObj.pop()
                    else:
                        nowLevels.append(sortTotal.pop())
                        objLevels.append(sortObj.pop())
#                print k,': nowLevels: ',nowLevels,' objLevels: ',objLevels
                for l in nowLevels:
                    nextBuildings.append((k,l+1))
    return nextBuildings
def getMaxCollision(nextBuildings,buildings,maxLoot):
    minBuildings = [9999999,9999999,9999999,9999999,9999999,9999999]
    #gold, elixir, dark_elixir
    for b in nextBuildings:
        bType = buildings[b[0]]['type']
        bCost = buildings[b[0]][b[1]]['cost']
        if bType is 'gold':
            if bCost < minBuildings[0]:
                minBuildings[0]=bCost
            elif bCost < minBuildings[1]:
                minBuildings[1]=bCost
        elif bType is 'elixir':
            if bCost < minBuildings[2]:
                minBuildings[2]=bCost
            elif bCost < minBuildings[3]:
                minBuildings[3]=bCost
        elif bType is 'dark_elixir':
            if bCost < minBuildings[4]:
                minBuildings[4]=bCost
            elif bCost < minBuildings[5]:
                minBuildings[5]=bCost
    return [math.floor(maxLoot['gold']/(minBuildings[0]+minBuildings[1])),math.floor(maxLoot['elixir']/(minBuildings[2]+minBuildings[3])),math.floor(maxLoot['dark_elixir']/(minBuildings[4]+minBuildings[5]))]

def finish(now,working,obj):
    keys=obj.keys()
    #keys denote all objective buildings
    for k in keys:
        if now.has_key(k):
            total=list(now[k])
        for w in working:
            if w[0] is k:
                for i in range(len(total)):
                    if total[i] is w[1]-1 and w[2] is nextWorker:
                        total[i]=total[i]+1
                        break
                    elif total[i] is w[1]-1:
                        total[i]=total[i]+999
        if total is not obj[k]:
            return False
    return True

def getTimeInterval(nextWorker):
    return nextWorker

def addLoot(loot,earn,timeInterval):
    newLoot={}
    for r in loot.keys():
        newLoot[r]=loot[r]+earn[r]*timeInterval
    return newLoot

def addTime(time,timeInterval):
    return time+timeInterval

def upWorker(nextBuilding,buildings,worker,timeInterval):
    """
    worker: [3, 0, 0, 1, 2]
    nextBuilding: ('mortar', 1) --> 6
    timeInterval: 1
    """
    W = sorted([0 if w == 0 else max(w-timeInterval, 0) for w in worker])
    W.pop(0)

    bn, blv = nextBuilding
    W.append( buildings[bn][blv]['time'] )

    return W

def getMaxInterval(nextBuilding,buildings,maxLoot,loot,earn):
    maxBuildings = [0,0,0]
    #gold, elixir, dark_elixir
    for b in nextBuildings:
        bType = buildings[b[0]]['type']
        bCost = buildings[b[0]][b[1]]['cost']
        if bType is 'gold':
            if bCost > maxBuildings[0]:
                maxBuildings[0]=bCost
        elif bType is 'elixir':
            if bCost > maxBuildings[1]:
                maxBuildings[1]=bCost
        elif bType is 'dark_elixir':
            if bCost > maxBuildings[2]:
                maxBuildings[2]=bCost
    return [math.floor(max(maxBuildings[0],maxLoot['gold']-loot['gold'])/earn['gold']),math.floor(max(maxBuildings[1],maxLoot['elixir']-loot['elixir'])/earn['elixir']),math.floor(max(maxBuildings[2],maxLoot['dark_elixir']-loot['dark_elixir'])/earn['dark_elixir'])]

def getMinInterval(nextBuildings,buildings,earn):
    minBuildings = [9999999,9999999,9999999]
    #gold, elixir, dark_elixir
    for b in nextBuildings:
        bType = buildings[b[0]]['type']
        bCost = buildings[b[0]][b[1]]['cost']
        if bType is 'gold':
            if bCost < minBuildings[0]:
                minBuildings[0]=bCost
        elif bType is 'elixir':
            if bCost < minBuildings[1]:
                minBuildings[1]=bCost
        elif bType is 'dark_elixir':
            if bCost < minBuildings[2]:
                minBuildings[2]=bCost
        if minBuildings[0] is 9999999:
            minBuildings[0] = 0
        if minBuildings[1] is 9999999:
            minBuildings[1] = 0
        if minBuildings[2] is 9999999:
            minBuildings[2] = 0
    return [math.floor(minBuildings[0]/earn['gold']),math.floor(minBuildings[1]/earn['elixir']),math.floor(minBuildings[2]/earn['dark_elixir'])]


def findAvailable(nextBuildings,buildings,loot,minInterval,maxInterval,maxCollision,worker,working):
    available = []
    for b in nextBuildings:
        bType = buildings[b[0]]['type']
        bCost = buildings[b[0]][b[1]]['cost']
        bTime = buildings[b[0]][b[1]]['time']
        if bType is 'gold':
            bi=0;
        elif bType is 'elixir':
            bi=1;
        elif bType is 'dark_elixir':
            bi=2;
        interval = getInterval(bTime,working,buildings,bType)
        if interval is 0:
            collision = getCollision(worker,bTime,working,buildings,bType)
        else:
            collision = 0
#        print 'name: ',b[0],' ,type: ',bType,' ,cost: ',bCost,' time: ',bTime
#        print 'interval: ',interval,' collision: ',collision
        if bCost<loot[bType] and interval>=minInterval[bi] and interval<=maxInterval[bi] and collision<=maxCollision[bi]:
            available.append(b)
    return available
    
def getInterval(bTime,working,buildings,bType):
    working=sorted(working,key=lambda x: x[2])
    newWorker=[]
    nextWorker=working[0][2]+bTime
    interval=999
    #sort by time remaining
    for w in range(1,len(working)):
        if buildings[working[w][0]]['type'] is bType:
            newWorker.append(working[w][2]+bTime)
#    print 'newWorker: ',newWorker
    for t in newWorker:
        if abs(nextWorker-t) < interval:
            interval = abs(nextWorker-t)
    return interval
def getCollision(worker,bTime,working,buildings,bType):
    working=sorted(working,key=lambda x: x[2])
    newWorker=[]
    nextWorker=working[0][2]+bTime
    collision=0
    #sort by time remaining
    for w in range(1,len(working)):
        if buildings[working[w][0]]['type'] is bType:
            newWorker.append(working[w][2]+bTime)
    for t in newWorker:
        if abs(nextWorker-t) is 0:
            collision = collision + 1
    return collision

def findBest(available,working,buildings,earn,bound):
    load = [0,0,0]
    t = [];
    
    for w in working:
        if buildings[w[0]]['type'] is 'gold':
            bi=0;
        elif buildings[w[0]]['type'] is 'elixir':
            bi=1;
        elif buildings[w[0]]['type'] is 'dark_elixir':
            bi=2;
        load[bi] = load[bi] + buildings[w[0]][w[1]]['cost']/buildings[w[0]][w[1]]['time']
#    print 'load: ',load
    for a in available:
        t.append(abs(earn[buildings[a[0]]['type']]*(1+bound)-(load[0]+buildings[a[0]][a[1]]['cost']/buildings[a[0]][a[1]]['time'])))
#    print 't: ',t
    return available[t.index(min(t))]

def upWorking(working, nextBuilding, building, worker, timeInterval):
    """
    nextBuilding:   ('cannon', 1)
    buildings:      {'mortar':{'type':'gold',1:{'cost':1600000,'time':6},2:{'cost':3200000,'time':7}}}
    worker:         [5, 1, 2, 3, 4]
    working:        [('camp', 1, 1), ('mortar', 2, 2), ('camp', 1, 3), ('cannon', 1, 4), ('camp', 1, 5)]

    working:        [('camp', 1, 0), ('mortar', 2, 1), ('camp', 1, 3), ('cannon', 1, 4), ('camp', 1, 5)]

    working:        [('camp', 1, 0), ('mortar', 2, 0), ('camp', 1, 2), ('cannon', 1, 3), ('camp', 1, 4)]
    """
    # update currernt working list
    new_working = sorted( [(name, lv, 0 if remaining == 0 else max(remaining-timeInterval,0) ) for name, lv, remaining in working], key=lambda x:x[2])
    new_working.pop(0)


    # insert the next building into the working list
    bn, blv = nextBuilding    
    new_working.append(( bn, blv, buildings[bn][blv]['time'] ))

    return sorted(new_working, key=lambda x:x[2])

def upNow(working,now):
    working=sorted(working,key=lambda x: x[2])
    newNow = now
    if newNow.has_key(working[0][0]):
        for li in range(len(newNow[working[0][0]])):
            if newNow[working[0][0]][li] is working[0][1]-1:
                newNow[working[0][0]][li] = working[0][1]
                break
    else:
        newNow[working[0][0]]=[working[0][1]]
    return newNow

def getRequire(nextBuilding,buildings,loot):
    require = [0,0,0]
    if buildings[nextBuilding[0]]['type'] is 'gold':
        require[0] = max(0,loot['gold']-buildings[nextBuilding[0]][nextBuilding[1]]['cost'])
    if buildings[nextBuilding[0]]['type'] is 'elixir':
        require[1] = max(0,loot['elixir']-buildings[nextBuilding[0]][nextBuilding[1]]['cost'])
    if buildings[nextBuilding[0]]['type'] is 'gold':
        require[2] = max(0,loot['dark_elixir']-buildings[nextBuilding[0]][nextBuilding[1]]['cost'])
    return require

def getPausedTime(pausedTime):
    return 1+pausedTime

def waitWorker(waitTime,worker):
    return [ w-waitTime if w-waitTime >= 0 else 0 for w in worker]

def waitWorking(waitTime, working):
    """
    Parameters
    ==========
    waitTime: int
        e.g., 1
    working: list
        e.g., [('cannon', 1, 2), ('cannon', 1, 2), ('camp', 1, 2), ('mortar', 1, 3), ('mortar', 1, 3)]

    Returns
    =======
    updated working list

    Example
    =======
    e.g.,
        (input) working: [('cannon', 1, 2), ('cannon', 1, 2), ('camp', 1, 2), ('mortar', 1, 3), ('mortar', 1, 3)]
        (return)         [('cannon', 1, 1), ('cannon', 1, 1), ('camp', 1, 1), ('mortar', 1, 2), ('mortar', 1, 2)]
    e.g.,
        (input) working: [('cannon', 1, 0), ('cannon', 1, 0), ('camp', 1, 0), ('mortar', 1, 1), ('mortar', 1, 1)]
        (return)         [('cannon', 1, 0), ('cannon', 1, 0), ('camp', 1, 0), ('mortar', 1, 0), ('mortar', 1, 0)]
    """
    return [(name, level, remaining-waitTime if remaining-waitTime >= 0 else remaining) for name, level, remaining in working]


def examinigDone(working,now):
    newNow=dict(now)
    for name, level, remaining in filter(lambda x:x[2] == 0, working):
        # create value
        if name not in now:
            newNow[name] = [level]
        # update value
        else:
            newNow[name] = update_level(current_levels=now[name], new_level=level)
 
        # update `new_working` values
    working = filter(lambda x:x[2] > 0, working)
    return newNow


def update_level(current_levels, new_level):
    """
    Parameters
    ==========
    current_levels: list
        e.g., [0,0,0,0]
    new_level: int
        e.g., 1
 
    Return
    ======
    list: [1,0,0,0]
 
    Example
    =======
    update_level([0,0,0,0], 1): [1, 0, 0, 0]
    update_level([0,1,2,3], 2): [0, 2, 2, 3]
    """
    try:
        idx = current_levels.index(new_level-1)
        current_levels[idx] = new_level
    except ValueError:
        # new_level-1 is not in the current_levels
        pass
    return current_levels

def updater(now, working, worker, nextBuilding, buildings, pausedTime):
    """
    Function
    ========
    Update `now`, `working`, `worker` lists

    Parameters
    ==========
    working = [('mortar',2,1), ('camp',1,2), ('mortar',2,3), ('camp',1,4), ('camp',1,5)]
    worker = [1,2,3,4,5]
    now = {'mortar':[1,1,1,0],'cannon':[0,0,0,0]}
    nextBuilding = ('cannon', 1) 
    pausedTime = 1

    Expected outputs
    ================
    > input
    working : [('mortar',2,1), ('camp',1,2), ('mortar',2,3), ('camp',1,4), ('camp',1,5)]
     
    > subtract `pausedTime`
    working: [('mortar',2,0), ('camp',1,1), ('mortar',2,2), ('camp',1,3), ('camp',1,4)]
     
    > emit ('mortar',2,0)
    working: [('camp',1,1), ('mortar',2,2), ('camp',1,3), ('camp',1,4)]
     
    > add ('cannon', 1, ?)  ## ? is obtained from `buildings.json`
    working: [('camp',1,1), ('mortar',2,2), ('camp',1,3), ('camp',1,4), ('cannon', 1, 1)]

    """
    ## update `now`
    for name, level, remaining in filter(lambda x:max(x[2]-pausedTime,0) == 0, working):
        # create value
        if name not in now:
            now[name] = [level]
        # update value
        else:
            now[name] = update_level(current_levels=now[name], new_level=level) 
        # update `new_working` values

    ## update `working`
    # 1. subtract `pausedTime`
    working = [ (name, level, max(remaining - pausedTime ,0) ) for name, level, remaining in working ]

    # 2. emit element(s) with zero remaining day, i.e., `completed`
    completed = filter(lambda x:x[2] == 0, working)
    working = filter(lambda x:x[2] > 0, working)

    # 3.1 lookup next remaining
    next_name, next_level = nextBuilding
    next_remaining = buildings[next_name][next_level]['time']

    # 3.2 add `nextBuilding`
    working.append( (next_name, next_level, next_remaining) )



    ## update worker
    # worker = lambda x:max(x[2]-pausedTime,0), working    

    # return 




if __name__ == '__main__':
    
    nextBuildings = getNextBuildings(now,working,obj,nextWorker)
    # print 'nextBuildings: ',nextBuildings
    maxCollision = getMaxCollision(nextBuildings,buildings,maxLoot)
    # print 'getMaxCollision: ',maxCollision
    time = 0
    tempTI = 0
    while not finish(now,working,obj):
        timeInterval = getTimeInterval(nextWorker) + tempTI
        tempTI = timeInterval
        loot = addLoot(loot,earn,timeInterval)
        time = addTime(time,timeInterval)
        minInterval = getMinInterval(nextBuildings,buildings,earn)
        maxInterval = getMaxInterval(nextBuildings,buildings,maxLoot,loot,earn)
    #    print 'maxInterval: ',maxInterval,',minInterval: ',minInterval
        available = findAvailable(nextBuildings,buildings,loot,minInterval,maxInterval,maxCollision,worker,working)
    #    print 'available: ',available
    #    print '>'*20
    #    print 'timeInterval:',timeInterval
    #    print 'time:',time
    #    print 'tempTI:',tempTI

    #    print '<'*20

        if available:
            if len(available) == 1:
                nextBuilding = available
            else:
                nextBuilding = findBest(available,working,buildings,earn,bound)
        #    
    #        print 'nextBuilding:',nextBuilding
    #        worker = upWorker(nextBuilding,buildings,worker,timeInterval)
            # print 'worker:',worker

    #        now = upNow(working,now)
    #        print 'now:',now

    #        print '>> working', working
    #        working = upWorking(working, nextBuilding,buildings,worker, timeInterval)
    #        print '<< working:',working

            require=getRequire(nextBuilding,buildings,loot)
            
            bn, blv = nextBuilding
            print 'Start build:',bn
            print 'level:',blv
            print 'require:',buildings[bn][blv]['cost'],' ',buildings[bn]['type']
            try:
                print 'require per day:',[require[0]/timeInterval,require[1]/timeInterval,require[2]/timeInterval]
            except ZeroDivisionError:
                print 'wtf'
            tempTI = 0
            pausedTime=timeInterval
        else:
            pausedTime=getPausedTime(pausedTime)
    #        worker=waitWorker(waitTime,worker)

    #        working=waitWorking(waitTime,working)

    #        now=examinigDone(working,now)
    #        print 'else'
            # no available building waiting resourse 
            # TBD
        print '===before==='
        print 'worker:',worker
        print 'working:',working
        print 'now:',now
        print '============'
        updater(now, working, worker, nextBuilding, buildings, pausedTime)
        print '===after==='
        print 'worker:',worker
        print 'working:',working
        print 'now:',now
        print '============'
        sortedWorker = sorted(worker)
        nextWorker = sortedWorker[0]
        
        # print 'working: ',working
        raw_input()

    print 'Done!'
