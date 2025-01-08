import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("red")
pen.speed(3)

# Function to draw the heart
def draw_heart():
    pen.begin_fill()
    
    pen.left(50)
    pen.forward(133)
    
    pen.circle(50, 200)
    
    pen.right(140)
    pen.circle(50, 200)
    
    pen.forward(133)
    
    pen.end_fill()

# Move the pen to a starting position
pen.penup()
pen.setpos(0, -100)
pen.pendown()

# Draw the heart
draw_heart()

# Hide the turtle
pen.hideturtle()

# Finish
turtle.done()
