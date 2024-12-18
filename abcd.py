import turtle

t = turtle.Turtle()

t.speed(0)
turtle.bgcolor("black")

colors = ['red', 'yellow', 'blue', 'green', 'purple', 'orange']

for i in range (60):
    t.color(colors[i%6])
    t.forward(i*10)
    t.right(144)

turtle.done()