# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 16:10:42 2019

@author: Administrator
"""
import turtle as t

t.pensize(12)

#画一个长为200宽为150的矩形
t.up()
t.goto(-100,75)
t.down()

t.fd(200)
t.right(90)
t.fd(150)
t.right(90)
t.fd(200)
t.right(90)
t.fd(150)

# 左脚1
t.up()
t.goto(-100,20)
t.down()

t.left(65)
t.fd(50)
t.left(75)
t.fd(30)

# 左脚2
t.right(140)#将箭头朝向上方

t.up()
t.goto(-100,-5)
t.down()

t.left(75)
t.fd(45)
t.left(65)
t.fd(30)
# 左脚3
t.right(140)
t.up()
t.goto(-100,-30)
t.down()

t.left(90)
t.fd(40)
t.left(55)
t.fd(30)

# 左脚4
t.right(145)
t.up()
t.goto(-100,-50)
t.down()

t.left(120)
t.fd(40)
t.left(45)
t.fd(30)

t.right(165)

# 右脚1
t.up()
t.goto(100,20)
t.down()

t.right(65)
t.fd(50)
t.right(75)
t.fd(30)
# 右脚2
t.left(140)
t.up()
t.goto(100,-5)
t.down()

t.right(75)
t.fd(45)
t.right(65)
t.fd(30)
# 右脚3
t.left(140)
t.up()
t.goto(100,-30)
t.down()

t.right(90)
t.fd(40)
t.right(55)
t.fd(30)
# 右脚4
t.left(145)
t.up()
t.goto(100,-50)
t.down()

t.right(120)
t.fd(40)
t.right(45)
t.fd(30)

t.left(165)
#右眼
t.up()
t.goto(40,75)
t.down()

#t.fillcolor('black')
#t.begin_fill()
t.circle(10)
#t.end_fill()
#左眼

t.up()
t.goto(-30,75)
t.down()

#t.fillcolor('black')
#t.begin_fill()
t.circle(10)
#t.end_fill()

# 右钳
t.up()
t.goto(65,75)
t.down()

t.right(30)    #小手臂
t.fd(60)
t.bk(20)
t.left(60)
t.fd(20)

t.right(30)   #方向向上

#左钳
t.up()
t.goto(-65,75)
t.down()

t.left(30)
t.fd(40)

t.right(30)

t.fillcolor('red')
t.begin_fill()
t.right(90)
t.circle(30,160)
t.left(90)
t.fd(20)
t.right(160)
t.left(30)
t.fd(20)
t.left(90)
t.circle(30,160)
t.end_fill()
t.fillcolor('black')
t.left(80)
#嘴
t.up()
t.goto(50,20)
t.down()

t.left(90)
t.fd(100)
t.left(90)
t.circle(50,180)

t.done()














