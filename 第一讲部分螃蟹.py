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

# 右脚1
t.up()
t.goto(100,20)
t.down()
t.right(140)
t.right(65)
t.fd(50)
t.right(75)
t.fd(30)

#右眼
t.up()
t.goto(30,75)
t.down()
t.circle(10)


# 右钳
t.up()
t.goto(65,75)
t.down()
t.left(140)

t.right(30)    #小手臂
t.fd(60)
t.bk(20)
t.left(60)
t.fd(20)

t.right(30)   #方向向上


#嘴
t.up()
t.goto(50,20)
t.down()

t.left(90)
t.fd(100)
t.left(90)
t.circle(50,180)






