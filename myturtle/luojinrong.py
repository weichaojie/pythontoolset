#coding=utf-8
import turtle
import time
import random
import math

mypen = turtle.Pen()

print(u"武汉外国语学校小学部三六班")

#for each in range(4):
    #mypen.forward(180);
#    time.sleep(1);
    #mypen.right(90);

mypen.right(180)
mypen.forward(90)

random.seed(10);
for loop in range(150):
    forword_step = random.randint(1, 50);
    mypen.forward(forword_step);
    turn_degree = random.randint(1, 90);
    mypen.right(turn_degree % 90);

time.sleep(1);