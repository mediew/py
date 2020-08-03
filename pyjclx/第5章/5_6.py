print("--------------------------------------------")
print("   英里   |   公里   ||   英里   |   公里")
mile=1
kilometer=20
for i in range(10):
        print("--------------------------------------------")
        print("   ",format(mile,"2d"),"   ",end='')
        print("|",end='')
        print(" ",format(mile*1.609,">6.3f")," ",end='')
        print("||",end='')
        print(" ",format(kilometer/1.609,"6.3f"),"",end='')
        print("|",end='')
        print("   ",format(kilometer,"2d"),)
        mile+=1
        kilometer+=5
print("--------------------------------------------")
