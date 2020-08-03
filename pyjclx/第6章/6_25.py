def reverse(number):
        palindrome=''
        while number>0:
                palindrome+=str(number%10)
                number=number//10
        palindrome=int(palindrome)
        return palindrome
def isPalindrome(number):
        if number==reverse(number):
                return True
        else:
                return False
def isPrime(number):
        divisor=2
        while divisor<=number/2:
                if number%divisor==0:
                        return False
                else:
                        divisor+=1
        return True
def judgeBit(number):
        bit=0
        if number==0:
                return 1
        elif number!=0:
                while number!=0:
                        number//=10
                        bit+=1
        return bit
def main():
        i=1
        number=1
        testi=1
        testNumber=1
        while testi<=100:
                if isPrime(testNumber) and isPrime(reverse(testNumber)) \
                and not(isPalindrome(testNumber)):
                        testi+=1                        
                testNumber+=1
                bit=str(judgeBit(testNumber-1))
        while i<=100:
                if isPrime(number) and isPrime(reverse(number)) and not(isPalindrome(number)):
                        print(format(number,bit+"d"),"",end='')
                        i+=1
                        if (i-1)%10==0:
                                print()
                number+=1
main()
                
