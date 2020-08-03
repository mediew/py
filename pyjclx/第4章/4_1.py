a,b,c=eval(input("enter a,b,c:"))
if b**2-4*a*c>=0:
        if b**2-4*a*c==0:
           x0=-b/(a*2)
           print("The root is",x0)
        else:
           x1=(-b+(b*b-4*a*c)**0.5)/(2*a)
           x2=(-b-(b*b-4*a*c)**0.5)/(2*a)
           print("The roots are",x1,"and",x2)
else:
        print("The equation has no real roots")
