year=eval(input("enter a year:"))
firstday=eval(input("enter the day:"))
month=1
day=firstday
for a in range(12):
     date=1
     if month==1:
        monthname='january'
     elif month==2:
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
     print(format(monthname,">28s"),"",year)
     if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
             days=31
     elif month==4 or month==6 or month==9 or month==11:
             days=30
     else:
             if (year%4==0 and year%100!=0) or year%400==0:
                     days=29
             else:
                     days=28
     print("---------------------------------------------------------")
     print("sun     ","mon     ","tue     ","wed     ","thu     ","fri     ","sat")
     while date<=days:
        if date==1:
                for i in range(day):
                        print("         ",end='')
                if day==6:
                        print(format(date,">2d"))
                else:
                        print(format(date,">2d"),"      ",end='')
        else:
                if day==6:
                        print(format(date,">2d"))
                else:
                        print(format(date,">2d"),"      ",end='')
        day+=1
        day=day%7
        date+=1
     month+=1
     print()
