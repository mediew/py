def sumDigits(n):
        sum=0
        while n>0:
                sum+=(n%10)
                n=n//10
        return sum
def main():
        n=eval(input("enter an integer:"))
        print(sumDigits(n))
main()
