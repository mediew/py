a=0
for i in range(100,1001):
        if i%5==0 and i%6==0:
                a+=1
                if a%10==0:
                        print(i)
                else:
                        print(i,"",end='')

                
