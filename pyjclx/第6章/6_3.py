def reverse(number):
        palindrome=''
        while number>0:
                palindrome+=str(number%10)
                number=number//10
        palindrome=int(palindrome)
        return palindrome
def isPalindrome(number):
        if number==reverse(number):
                print("this number is palindrome!")
        else:
                print("this number isn't palindrome!")
def main():
        number=eval(input("enter an integer:"))
        isPalindrome(number)
main()
        
