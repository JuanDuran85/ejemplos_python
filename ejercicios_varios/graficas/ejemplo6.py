import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("white")
t.pencolor("blue")
t.speed(0)

for i in range(150):
    t.circle(190-1,90)
    t.lt(98)
    t.circle(190-1,90)
    t.lt(18)
    
turtle.done()