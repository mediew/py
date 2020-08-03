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
print("your amount",amount,"consist of\n",
      "\t",numberOFOneDollars,"dollars\n"
      "\t",numberOFQuarters,"quarters\n"
      "\t",numberOFDimes,"dimes\n"
      "\t",numberOFNikles,"nikles\n"
      "\t",numberOFPennies,"pennies")
