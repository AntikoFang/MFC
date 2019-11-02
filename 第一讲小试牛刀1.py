import turtle as t

# 写了一个移动画笔的函数
def GoTo(x,y):
    t.up()
    t.goto(x, y)
    t.down()

#准备工作
GoTo(0,100)            #设置起点       可直接调用之前写的移动画笔的函数
t.pencolor('gray')    #设置小人颜色
t.pensize(50)          #设置画笔粗细

#画小人的头
t.circle(15)

GoTo(-50,50)   #移动到测量好的身体坐标

#画小人的手臂
t.right(20)   #倾斜角度可自由发挥，比例大致相同即可
t.fd(60)
t.right(30)
t.fd(50)
t.left(50)
t.fd(60)

#画小人的背
t.right(110)
GoTo(-25,30)
t.pensize(100)
t.fd(100)

#画小人的腿
GoTo(-90,-80)
t.left(90)
t.pensize(50)
t.fd(100)
t.right(90)
t.fd(80)

#自行车前轮
GoTo(60,-140)
t.pencolor('red')
t.pensize(10)
t.circle(60)

#自行车后轮
GoTo(-210,-140)
t.pencolor('red')
t.pensize(10)
t.circle(60)

t.fillcolor('red')   #隐藏画笔

t.done()