from turtle import begin_fill, circle, color, done, end_fill, goto, hideturtle, speed, penup, pendown, forward

speed(100)

def instal(x,y):
    penup()
    goto(x,y)
    pendown()

def instal_two(x,y,f,c,c1,c2):
    color(c)
    instal(x,y)
    begin_fill()
    for _ in range(4):
        forward(f)
        circle(c1,c2)
    end_fill()
def instal_three(c,x,y,c1):
    color(c)
    begin_fill()
    instal(x,y)
    circle(c1)
    end_fill()

instal_two(-150,-120,350,"pink",20,90)
instal_two(-110,-70,260,"white",20,90)
instal_two(-90,-50,220,"pink",20,90)
instal_three("white",20,10,70)
instal_three("pink",20,30,50)
instal_three("white",110,160,15)
hideturtle()
done()