def displayPattern(n):
        testNumber=n
        count=0
        while testNumber>0:
                testNumber//=10
                count+=1
        row=1
        for i in range(n):
                for a in range((n-row)*(count+1)):
                        print(" ",end='')
                for b in range(row):
                        print(format((row-b),'>'+str(count)+'d'),"",end='')
                        if b==(row-1):
                                print()
                row+=1
def main():
        n=eval(input("enter an integer:"))
        displayPattern(n)
main()
