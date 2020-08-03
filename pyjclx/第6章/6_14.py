def itom(i):
        sum=0
        while i>=1:
                sum=sum+((-1)**(i+1))/(2*i-1)
                i=i-1
        m=4*sum
        return m
def printab():
        print("------------------------------")
        print("      i      |      m(i)")
        for i in range(1,1001,100):
                print("------------------------------")
                print("    ",format(i,">3d"),"    |    ",format(itom(i),">6.4f"))
        print("------------------------------")
printab()
