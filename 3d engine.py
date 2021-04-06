import turtle
import time

pen = turtle.Pen()
def plane(xw,yw,x,y,z,a):
    if a != 0:
        pen.up()
        pen.setheading(0)
        pen.goto((x+(z*5),y+(z*5))
        xp = 0
        yp = 0
        pen.down()
        pen.forward(xw-(z*5))
        pen.goto((x+(z*5),y+(z*5)))
        pen.left(90-a*10)
        pen.forward((yw/a)-(z*5))
        xp = pen.xcor()
        yp = pen.ycor()
        pen.goto((x+(z*5),y+(z*5)))
        pen.right(90-a*10)
        pen.forward(xw-z)
        pen.left(90+a*10)
        pen.forward((yw/a)-(z*5))
        pen.goto((xp,yp))

        

    if a == 0:
        pen.up()
        pen.setheading(0)
        pen.goto((x+(z*5),y+(z*5)))
        xp = 0
        yp = 0
        pen.down()
        pen.forward(xw-(z*5))
        pen.goto((x+(z*5),y+(z*5)))
        pen.left(90-a*10)
        pen.forward((yw/1)-(z*5))
        xp = pen.xcor()
        yp = pen.ycor()
        pen.goto((x+(z*5),y+(z*5)))
        pen.right(90-a*10)
        pen.forward(xw-z)
        pen.left(90+a*10)
        pen.forward((yw/1)-(z*5))
        pen.goto((xp,yp))
        
        
        
    
 
plane(100,200,0,0,3,4)
time.sleep(5)

