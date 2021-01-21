import turtle
import math
bob = turtle.Turtle()
# print(bob)


def square(t, l):
    for i in range(4):
        t.fd(l)
        t.lt(90)
# square(bob, 120)


def polygon(t, l, n):
    for i in range(n):
        t.fd(l)
        t.lt(360/n)
# polygon(bob, 100, 7)


def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, length, n)
# circle(bob, 100)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    for i in range(n):
        t.lt(step_angle)
        t.fd(step_length)


'''
a = 90
for i in range(1):
    arc(bob, 100, a)
    bob.lt(180-a)
'''


def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)


draw(bob, 10, 3)
# radius = 100
# bob.pu()	# 抬笔
# bob.fd(radius)
# bob.lt(90)
# bob.pd()	# 落笔
turtle.Screen().mainloop()   # 不关闭窗口
