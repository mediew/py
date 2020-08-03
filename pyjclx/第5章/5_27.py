max=eval(input("enter a large number:"))
sum=0
i=1
while i<=max:
        sum+=(-1)**(i+1)/(2*i-1)
        i+=1
print("pi is around",sum*4)
