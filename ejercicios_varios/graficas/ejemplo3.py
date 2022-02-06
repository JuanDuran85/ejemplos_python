import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("lightgreen")
t.pencolor("blue")
t.speed(100)

colors = ("red", "orange", "yellow", "green")

for n in range(10):
    for x in range(8):
        t.speed(x+10)
        for i in range(2):
            t.pensize(2)
            t.circle(80+n*20,90)
            t.lt(90)
        t.lt(45)
    t.pencolor(colors[n%4])
s.exitonclick()