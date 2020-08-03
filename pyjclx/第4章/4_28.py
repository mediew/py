x1,y1,w1,h1=eval(input("enter r1's center x-,y-coordinates,width,and height:"))
x2,y2,w2,h2=eval(input("enter r2's center x-,y-coordinates,width,and height:"))

distence_x=abs(x1-x2)
distence_y=abs(y1-y2)
min_x=0.5*abs(w1-w2)
max_x=0.5*abs(w1+w2)
min_y=0.5*abs(h1-h2)
max_y=0.5*abs(h1+h2)

if distence_x<=min_x and distence_y<=min_y:
        if w1<w2:
                print("r1 is inside r2")
        elif w1==w2:
                print("r1=r2")
        else:
                print("r2 is inside r1")
elif distence_x>=max_x or distence_y>=max_y:
        print("r2 does not overlap r1")
else:
        print("r2 overlaps r1")
print("the graphic is following...")
import turtle
turtle.penup()
turtle.goto(x1-0.5*w1,y1+0.5*h1)
turtle.pendown()
turtle.goto(x1+0.5*w1,y1+0.5*h1)
turtle.goto(x1+0.5*w1,y1-0.5*h1)
turtle.goto(x1-0.5*w1,y1-0.5*h1)
turtle.goto(x1-0.5*w1,y1+0.5*h1)
turtle.penup()
turtle.goto(x2-0.5*w2,y2+0.5*h2)
turtle.pendown()
turtle.goto(x2+0.5*w2,y2+0.5*h2)
turtle.goto(x2+0.5*w2,y2-0.5*h2)
turtle.goto(x2-0.5*w2,y2-0.5*h2)
turtle.goto(x2-0.5*w2,y2+0.5*h2)
turtle.done()
