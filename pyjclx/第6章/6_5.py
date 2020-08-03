def displaySortedNumbers(num1,num2,num3):
        if num1>num2:
                num1,num2=num2,num1
                if num2>num3:
                        num2,num3=num3,num2
                        if num2<num1:
                                num1,num2=num2,num1
        else:
                if num2>num3:
                        num2,num3=num3,num2
                        if num2<num1:
                                num1,num2=num2,num1
        print(num1,num2,num3)
def main():
        num1,num2,num3=eval(input("enter three numbers:"))
        displaySortedNumbers(num1,num2,num3)
main()


