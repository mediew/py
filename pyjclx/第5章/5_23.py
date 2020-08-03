loanAmount=eval(input("loan amount:"))
numberofyear=eval(input("number of years:"))
interestRate=0.05

print("interest rate   ","monthly payment   ","total payment")
for i in range(25):
        monthlyInterestRate=interestRate/12
        monthlyPayment=loanAmount*monthlyInterestRate/(1-1/(1+monthlyInterestRate)**(numberofyear*12))
        totalPayment=monthlyPayment*numberofyear*12
        print(format(interestRate,"<16.3%"),format(monthlyPayment,"<18.2f"),format(totalPayment,"<8.2f"))
        interestRate+=0.00125
