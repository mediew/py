integer=eval(input("Enter an integer:"))
a=integer//1000
remain=integer%1000
b=remain//100
remain=remain%100
c=remain//10
remain=remain%10
reversedNumber=remain*1000+c*100+b*10+a
print("The reversed number is",reversedNumber)
