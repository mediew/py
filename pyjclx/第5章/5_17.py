collum=0
for i in range(33,127):
        collum+=1
        if collum%10==0:
                print(chr(i))
        else:
                print(chr(i),"",end='')
