a,b,c=eval(input("enter three integers:"))
if a>=b:
        a,b=b,a
        if b>=c:
                b,c=c,b
                if a>=b:
                        a,b=b,a
else:
        if b>=c:
                b,c=c,b
                if a>=b:
                        a,b=b,a
print(a,b,c)
