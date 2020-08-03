def returnSortedNumbers(num1,num2,num3):
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
        return num1,num2,num3
def isValid(side1,side2,side3):
        
        min,mid,max=returnSortedNumbers(side1,side2,side3)
        if min+mid>max:
                return True
        else:
                return False
def area(side1,side2,side3):
        
        if isValid(side1,side2,side3):
                s=(side1+side2+side3)/2
                import math
                area=pow((s*(s-side1)*(s-side2)*(s-side3)),0.5)
                print("the area of the triangle is",area)
        else:
                print("input is invalid")
        
def main():
        side1,side2,side3=eval(input("enter three sides in double:"))
        area(side1,side2,side3)
main()
