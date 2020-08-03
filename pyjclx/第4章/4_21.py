year=eval(input("enter year:(e.g.,2008):"))
m=eval(input("enter the month:1-12:"))
q=eval(input("enter the day of the month:1-31:"))
if m<3:
        m=m+12
        year=year-1
k=year%100
j=year//100
h=(q+26*(m+1)//10+k+k//4+j//4+5*j)%7
if h==0:
        print("day of the week is saturday")
elif h==1:
        print("day of the week is sunday")
elif h==2:
        print("day of the week is monday")
elif h==3:
        print("day of the week is tuesday")
elif h==4:
        print("day of the week is wednesday")
elif h==5:
        print("day of the week is thursday")
else:
        print("day of the week is friday")
