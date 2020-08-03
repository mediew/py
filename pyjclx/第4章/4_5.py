day=eval(input("enter today's day:"))
if day==0:
        currentday='sunday'
elif day==1:
        currentday='monday'
elif day==2:
        currentday='tuesday'
elif day==3:
        currentday='wednesday'
elif day==4:
        currentday='thursday'
elif day==5:
        currentday='friday'
elif day==6:
        currentday='saturday'
else:
        print("please enter the correct day")
number=eval(input("enter the number of days elapsed since today:"))
if (day+number)%7==0:
        print("today is",currentday,"and the future day is sunday")
elif (day+number)%7==1:
        print("today is",currentday,"and the future day is monday")
elif (day+number)%7==2:
        print("today is",currentday,"and the future day is tuesday")
elif (day+number)%7==3:
        print("today is",currentday,"and the future day is wednesday")
elif (day+number)%7==4:
        print("today is",currentday,"and the future day is thursday")
elif (day+number)%7==5:
        print("today is",currentday,"and the future day is friday")
else:
        print("today is",currentday,"and the future day is saturday")
