amount=eval(input("Enter an amount, for example, 1156:"))
import math
numberOFOneDollars=amount//100
remainingAmount=amount%100
numberOFQuarters=remainingAmount//25
remainingAmount=remainingAmount%25
numberOFDimes=remainingAmount//10
remainingAmount=remainingAmount%10
numberOFNikles=remainingAmount//5
remainingAmount=remainingAmount%5
numberOFPennies=remainingAmount
if numberOFOneDollars==1:
        numberOFOneDollars=str(numberOFOneDollars)+' dollar'
else:
        numberOFOneDollars=str(numberOFOneDollars)+' dollars'
if numberOFQuarters==1:
        numberOFQuarters=str(numberOFQuarters)+' quarter'
else:
        numberOFQuarters=str(numberOFQuarters)+' quarters'
if numberOFDimes==1:
        numberOFDimes=str(numberOFDimes)+' dime'
else:
        numberOFDimes=str(numberOFDimes)+' dimes'
if numberOFNikles==1:
        numberOFNikles=str(numberOFNikles)+' nikle'
else:
        numberOFNikles=str(numberOFNikles)+' nikles'
if numberOFPennies==1:
        numberOFPennies=str(numberOFPennies)+' penny'
else:
        numberOFPennies=str(numberOFPennies)+' pennies'
print("your amount",amount,"consist of\n",
      "\t",numberOFOneDollars,"\n"
      "\t",numberOFQuarters,"\n"
      "\t",numberOFDimes,"\n"
      "\t",numberOFNikles,"\n"
      "\t",numberOFPennies)
