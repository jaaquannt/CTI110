import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(2)
t.pensize(3)
t.color("green")

# Drawing the top (horizontal line) of "J"
t.penup()
t.goto(-75, 100)
t.setheading(0)
t.pendown()
t.forward(100)
# Move to the center of the horizontal line to start vertical line
t.penup()
t.goto(-25, 100)
t.setheading(270)
t.pendown()
t.forward(70)
# Drawing the curved bottom of "J"
t.circle(-25, 180)  # Small half-circle to create the bottom curve

# Move to a new position for "T"
t.penup()
t.goto(50, 100)
t.setheading(0)
t.pendown()

# Drawing "T"
t.forward(50)
t.backward(25)
t.setheading(270)
t.forward(100)
