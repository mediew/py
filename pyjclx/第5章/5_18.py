integer=eval(input("enter an integer:"))
divisor=2
while divisor<=integer/2:
        if integer%divisor==0:
                print(divisor,"",end='')
                integer=integer/divisor
        else:
                divisor+=1
print(int(integer))
