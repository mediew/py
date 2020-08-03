weight1,price1=eval(input("enter weight and price for package 1:"))
weight2,price2=eval(input("enter weight and price for package 2:"))
priceperweight1=price1/weight1
priceperweight2=price2/weight2
if priceperweight1>priceperweight2:
        print("package 2 has the better price.")
elif priceperweight1==priceperweight2:
        print("they have the same price.")
else:
        print("package 1 has the better price.")
