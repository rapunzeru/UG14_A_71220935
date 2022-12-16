import turtle
s= turtle.Screen()
t= turtle.Turtle()
t.pensize(10)
t.color('pink')

#D
t.circle(100, 180)
t.left(90)
t.forward(200)
t.right(90)


#9
t.penup()
t.goto(200, 200)
t.pendown()
t.circle(60)
t.left(180)
t.circle(-60, 90)
t.forward(100)
t.circle(-55, 180)

#3
t.penup()
t.goto(300, 200)
t.pendown()
t.right(90)
t.forward(40)
t.circle(-50, 180)
t.forward(40)
t.left(180)
t.forward(40)
t.circle(-50, 180)
t.forward(40)

#5
t.penup()
t.goto(420, 200)
t.pendown()
t.left(180)
t.forward(100)
t.right(180)
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(30)
t.circle(-70, 180)
t.forward(30)

#P
t.penup()
t.goto(540, 0)
t.pendown()
t.right(90)
t.forward(200)
t.right(90)
t.circle(-60, 180)




turtle.done()