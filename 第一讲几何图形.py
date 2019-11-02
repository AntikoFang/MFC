import turtle as t

#正方形
t.fd(100)
t.left(90)
t.fd(100)
t.left(90)
t.fd(100)
t.left(90)
t.fd(100)

#正方形循环
for i in range(4):
    t.fd(100)
    t.left(90)

#圆
t.penup()
t.goto(100,200)
t.pendown()
t.circle(10,360)

#四分之三圆
t.penup()
t.goto(200,-50)
t.pendown()
t.pensize(10)
t.circle(50,270)
t.left(90)
t.fd(50)
t.right(90)
t.fd(50)

#橙色五角星
t.penup()
t.goto(200,200)
t.pendown()
t.pensize(3)
t.pencolor('orange')
t.fillcolor('orange')
t.begin_fill()
for i in range(5):
    t.fd(100)
    t.left(144)
t.end_fill()

t.done()

# 右钳
import turtle as t
t.up()
t.goto(65,75)
t.down()

t.right(30)
t.fd(40)

t.left(30)

t.left(30)
t.fd(20)

t.right(30)

t.right(120)
t.fd(10)
t.left(120)
t.right(60)
t.fd(10)

t.left(60)

t.left(150)
t.fd(20)

t.right(150)

# 右钳
import turtle as t
t.pensize(12)
t.up()
t.goto(65,75)
t.down()

t.right(30)    #小手臂
t.fd(40)

t.left(30)    #方向向上

t.left(30)
t.fd(20)
t.bk(20)
t.right(60)
t.fd(20)
t.done()

t.left(30)




