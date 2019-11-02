import turtle as t

# 写了一个移动画笔的函数
def GoTo(x,y):
    t.up()
    t.goto(x, y)
    t.down()

# 准备工作
GoTo(-100,100)            #设置起点       可直接调用之前写的移动画笔的函数
#t.pencolor()          #设置画笔颜色
t.pensize(40)          #设置画笔粗细

# 画左边的小人
#==============================
# 画小人的头
t.circle(13)

# 画小人的身体
GoTo(-130,50)

t.right(105)
t.pensize(60)
t.fd(80)

# 画小人的左腿
t.pensize(32)
GoTo(-170,-35)
t.fd(100)

# 画小人的右腿
GoTo(-140,-48)
t.left(45)
t.fd(40)
t.right(30)
t.fd(50)

# 画小人的手臂
GoTo(-105,50)
t.left(60)
t.fd(90)

# 画右边的小人
#==============================
#画小人的左手
t.left(105)
t.fd(70)

# 画小人的身体
GoTo(-5,0)
t.right(60)
t.pensize(60)
t.fd(80)

# 画小人的左腿
t.pensize(32)
GoTo(78,30)
t.left(75)
t.fd(100)

# 画小人的右腿
GoTo(78,10)
t.right(30)
t.fd(90)

# 画小人的右手
GoTo(-5,-20)
t.right(105)
t.fd(55)
t.left(60)
t.fd(60)

# 画小人的头
GoTo(-75,-35)
t.circle(13)

t.done()