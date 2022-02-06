import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pensize()
t.speed(15)
colors = ['blue', 'red', 'green', 'yellow', 'orange', 'purple']

for i in range(6):
    for col in colors:
        t.color(col)
        t.circle(100)
        t.left(10)
        
turtle.done()