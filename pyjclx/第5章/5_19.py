i=1
row=eval(input("enter the number of lines:"))
while i<=row:
        
                for a in range(1,row+1-i):
                        print("    ",end='')
                left=i
                while left>=1:
                        print(format(left,">2d")," ",end='')
                        left-=1
                print(" ",end='')
                right=1
                while right<=i:
                        if right<=1:
                                right+=1
                        else:
                                print(format(right,"<2d")," ",end='')
                                right+=1
                print()
                i+=1
