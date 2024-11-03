import turtle

# Set up turtle
t = turtle.Turtle()
t.speed(2)  # Attmempt at changing speed

# Drawing a square using a for loop
for _ in range(4):
    t.forward(100)
    t.right(90) 

# Attempt at moving the turtle to a new position to start triangle
t.penup()
t.goto(-50, -50)
t.pendown()

# Drawing a triangle using a while loop
sides = 0
while sides < 3:
    t.forward(100)
    t.left(120) 
    sides = sides + 1
