from turtle import begin_fill, color, forward, left, pos, end_fill, done

color('red', 'yellow')
begin_fill()
while True:
    forward(250)
    left(190)
    if abs(pos()) < 1:
        break
end_fill()
done()