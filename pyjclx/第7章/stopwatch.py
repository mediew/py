import time
class stopwatch:
        def __init__(self,startTime=0,endTime=2):
                self.__startTime=startTime
                self.__endTime=endTime
        def getStartTime(self):
                return self.__startTime
        def getEndTime(self):
                return self.__endTime
        def start(self):
                self.__startTime=int(time.time())
        def stop(self):
                self.__endTime=int(time.time())
        def getElapsedTime(self):
                return (self.__endTime-self.__startTime)
        
