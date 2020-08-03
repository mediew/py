loanamount=eval(input("loan amount:"))
numberofyears=eval(input("number of years:"))
annualinterestrate=eval(input("annual interest rate:"))
monthlyinterestrate=annualinterestrate/12/100
monthlypayment=loanamount*monthlyinterestrate/(1-1/(1+monthlyinterestrate)**(numberofyears*12))
totalpayment=monthlypayment*12*numberofyears
print("monthly payment:",format(monthlypayment,"6.2f"))
print("total payment:",format(totalpayment,"8.2f"))
print()
print("payment#","\t","interest","\t","principal","\t","balance")
balance=loanamount
for i in range(1,numberofyears*12+1):
        interest=monthlyinterestrate*balance
        principal=monthlypayment-interest
        balance=balance-principal
        if balance<0.5:
                principal+=balance
                balance=0
        print(format(i,"<8d"),"\t",format(interest,"<8.2f"),
              "\t",format(principal,"<9.2f")
              ,"\t",format(balance,"<7.2f"))
