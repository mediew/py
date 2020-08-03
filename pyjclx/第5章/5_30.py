year=eval(input("enter a year:"))
firstday=eval(input("enter the day:"))
month=1
print("january 1,",year,"is tuesday")
if (year%4==0 and year%100!=0) or year%400==0:
        while month<=11:
                if month==1 or month==3 or month==5 or month==7 or month==8 or month==10:
                        firstday=(firstday+31)%7
                elif month==4 or month==6 or month==9 or month==11:
                        firstday=(firstday+30)%7
                else:
                        firstday=(firstday+29)%7
                month+=1
                if month==2:
                        monthname='february'
                elif month==3:
                        monthname='march'
                elif month==4:
                        monthname='april'
                elif month==5:
                        monthname='may'
                elif month==6:
                        monthname='june'
                elif month==7:
                        monthname='july'
                elif month==8:
                        monthname='august'
                elif month==9:
                        monthname='september'
                elif month==10:
                        monthname='october'
                elif month==11:
                        monthname='november'
                else:
                        monthname='december'
                if firstday==0:
                        dayname='sunday'
                elif firstday==1:
                        dayname='monday'
                elif firstday==2:
                        dayname='tuesday'
                elif firstday==3:
                        dayname='wednesday'
                elif firstday==4:
                        dayname='thursday'
                elif firstday==5:
                        dayname='friday'
                else:
                        dayname='saturday'
                print(monthname,"1,",year,"is",dayname)
else:
        while month<=11:
                if month==1 or month==3 or month==5 or month==7 or month==8 or month==10:
                        firstday=(firstday+31)%7
                elif month==4 or month==6 or month==9 or month==11:
                        firstday=(firstday+30)%7
                else:
                        firstday=(firstday+28)%7
                month+=1
                if month==2:
                        monthname='february'
                elif month==3:
                        monthname='march'
                elif month==4:
                        monthname='april'
                elif month==5:
                        monthname='may'
                elif month==6:
                        monthname='june'
                elif month==7:
                        monthname='july'
                elif month==8:
                        monthname='august'
                elif month==9:
                        monthname='september'
                elif month==10:
                        monthname='october'
                elif month==11:
                        monthname='november'
                else:
                        monthname='december'
                if firstday==0:
                        dayname='sunday'
                elif firstday==1:
                        dayname='monday'
                elif firstday==2:
                        dayname='tuesday'
                elif firstday==3:
                        dayname='wednesday'
                elif firstday==4:
                        dayname='thursday'
                elif firstday==5:
                        dayname='friday'
                else:
                        dayname='saturday'
                print(monthname,"1,",year,"is",dayname)
