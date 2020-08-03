class stock:
        def __init__(self,symbol='symbol',name='name',pcp=1.00,cp=2.00):
                self.__symbol=symbol
                self.__name=name
                self.__pcp=pcp
                self.__cp=cp
        def getName(self):
                return self.__name
        def getSymbol(self):
                return self.__symbol
        def getPcp(self,pcp):
                return self.__pcp
        def setPcp(self,pcp):
                self.__pcp=pcp
        def getCp(self,cp):
                return self.__cp
        def setCp(self,cp):
                self.__cp=cp
        def getChangePercent(self):
                changePercent=format((self.__cp-self.__pcp)/self.__pcp,"7.2%")
                return changePercent
