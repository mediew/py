side=eval(input("Enter the side:"))
import math
y=side*math.cos(math.radians(36))/math.cos(math.radians(54))
distance=side*2+side*math.cos(math.radians(72))*2
import turtle
turtle.penup()
turtle.sety(y)
turtle.right(72)
turtle.pendown()
turtle.forward(distance)
turtle.right(144)
turtle.forward(distance)
turtle.right(144)
turtle.forward(distance)
turtle.right(144)
turtle.forward(distance)
turtle.right(144)
turtle.forward(distance)
