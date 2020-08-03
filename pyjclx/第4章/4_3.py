a,b,c,d,e,f=eval(input("enter a,b,c,d,e,f:"))
if a*d-b*c!=0:
   x=(e*d-b*f)/(a*d-b*c)
   y=(a*f-e*c)/(a*d-b*c)
   print("x is",x,"and y is",y)
else:
   print("The equation has no solution")
