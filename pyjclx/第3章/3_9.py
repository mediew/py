name=input("Enter employee's name:")
hours=eval(input("Enter number of hours worked in a week:"))
payRate=eval(input("Enter hourly pay rate:"))
federalTAXRate=eval(input("Enter federal tax withholding rate:"))
stateTAXRate=eval(input("Enter state tax withholding rate:"))
grossPay=hours*payRate
federalWithholding=hours*payRate*federalTAXRate
stateWithholding=hours*payRate*stateTAXRate
totalDeduction=federalWithholding+stateWithholding
netPay=grossPay-totalDeduction
print("Employee Name:",name,"\n"
      "Hours Worked:",hours,"\n"
      "Pay Rate:",payRate,"\n"
      "Gross Pay:",grossPay,"\n"
      "Deductions:\n"
      "\t","Federal Withholding(",format(federalTAXRate,"5.1%"),"): $",federalWithholding,"\n"
      "\t","State Withholding(",format(stateTAXRate,"4.1%"),"): $",stateWithholding,"\n"
      "\t","Total Deduction: $",totalDeduction,"\n"
      "Net Pay: $",netPay)
