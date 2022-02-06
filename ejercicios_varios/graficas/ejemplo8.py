import turtle

t = turtle.Turtle()
s = turtle.Screen()

def draw_squere():
    for _ in range(4):
        t.forward(30)
        t.left(90)
    t.forward(30)
    
if __name__ == '__main__':
    s.setup(width=600, height=600)
    t.speed(100)
    for i in range(8):
        t.up()
        t.setpos(0,30*i)
        t.down()
        for j in range(8):
            if (i+j)%2 == 0:
                col = "black"
            else:
                col = "white"
            t.fillcolor(col)
            t.begin_fill()
            draw_squere()
            t.end_fill()
        t.hideturtle()
    turtle.done()
           