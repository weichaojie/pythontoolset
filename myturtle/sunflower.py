from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(258)
    left(144)
    if abs(pos()) < 1:
        break
end_fill()
done()
