#coding=utf-8
import turtle
import time
import random

print(u"武汉外国语学校小学部三六班--仁爱学堂")

mypen = turtle.Pen()
mypen.pensize(3)

#画笔的颜色
mycolor=["black","red","pink","blue","yellow"]
#向前前进的长度
forword_step = 150
#转角90度
turn_degree = 90

for loop in range(150):
    mypen.pencolor(mycolor[random.randint(0, len(mycolor)-1)])
    if (forword_step > 0):
        mypen.forward(forword_step)
        forword_step = forword_step - 10
        mypen.right(turn_degree)
        
time.sleep(10)
