import random
number1=random.randint(0,99)
number2=random.randint(0,99)
answer=eval(input("what is"+str(number1)+"*"+str(number2)+"?"))
if number1*number2==answer:
        print("you are correct!")
else:
        print("you are wrong.\n",\
              number1,"*",number2,"is",number1*number2,".")
