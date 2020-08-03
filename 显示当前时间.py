import time
currentTime=time.time()
totalSeconds=int(currentTime)
currentSeconds=totalSeconds%60
totalMinutes=totalSeconds//60
currrentMinutes=totalMinutes%60
totalHours=totalMinutes//60
currentHour=totalHours%24
print("current time is", currentHour, ":", currrentMinutes, ":",currentSeconds, "GMT")