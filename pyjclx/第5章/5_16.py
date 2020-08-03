n1=eval(input("enter an integer:"))
n2=eval(input("enter another integer:"))
if n1>n2:
        n1,n2=n2,n1
d=n1
while d>0:
        if n1%d==0 and n2%d==0:
                break
        d-=1
print(d)
