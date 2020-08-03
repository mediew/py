import math
# r is the distence from the center to a vertex
r=eval(input("Enter a length from the center to a vertex:"))
# s is side length of the pentagon
s=2*r*math.sin(math.pi/5)
area=5*s*s/(4*math.tan(math.pi/5))
print("The area of the pentagon is",area)
