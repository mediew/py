positivecount=0
negativecount=0
sum=0
integer=1
while integer!=0:
        integer=eval(input("enter an integer, the input ends if it is 0:"))
        if integer==0:
                continue
        elif integer>0:
                positivecount+=1
#debug code:                print("positives count",positivecount)
        else:
                negativecount+=1
#debug code:                print("negatives count",negativecount)
        sum+=integer
print("the number of positives is",positivecount)
print("the number of negatives is",negativecount)
print("the total is",sum)
print("the average is",sum/(positivecount+negativecount))
        
