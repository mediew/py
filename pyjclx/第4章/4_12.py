integer=eval(input("enter an integer:"))
print("is",integer,"divisible by 5 and 6?",\
      integer%5==0 and integer%6==0,"\n",\
      "is",integer,"divisible by 5 or 6?",integer%5==0 or integer%6==0,"\n",\
      "is",integer,"divisible by 5 or 6,but not both?",(integer%5==0 or integer%6==0) and \
      not(integer%5==0 and integer%6==0))
