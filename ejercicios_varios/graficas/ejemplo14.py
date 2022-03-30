"""_summary_

    Using turtle graphics to draw a heart.

"""

import turtle

pen: turtle.Turtle = turtle.Turtle()

def curve() -> None:
    for _ in range(200):
        pen.right(1)
        pen.forward(1)

def heart() -> None:
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()
    
def txt() -> None:
    pen.up()
    pen.setpos(-68,95)
    pen.down()
    pen.color('lightgreen')
    pen.write('Heart', font=('Arial', 16, 'normal'))

heart()
txt()
pen.ht()