import turtle

turtle.title("Racing turtle")

s = turtle.Screen()
s.setup(700,700)

s.tracer(0)

grass = turtle.Turtle()
grass.penup()
grass.goto(-350,200)
grass.color('green')
grass.pendown()

grass.begin_fill()
grass.fd(700)
grass.lt(90)
grass.fd(200)
grass.lt(90)
grass.fd(700)
grass.lt(90)
grass.fd(200)
grass.end_fill()


water = turtle.Turtle()
water.penup()
water.goto(-350,200)
water.color('blue')
water.pendown()

water.begin_fill()
water.fd(700)
water.rt(90)
water.fd(500)
water.rt(90)
water.fd(700)
water.rt(90)
water.fd(500)
water.end_fill()

finish = turtle.Turtle()
finish.shape('circle')
finish.shapesize(0.01,0.01,0.01)
finish.color('gold')
finish.pensize(8)

finish.penup()
finish.goto(300,200) # x=300 finish
finish.down()
finish.right(90)
finish.forward(500)
finish.write('FINISH \nLINE  ', font=("Verdana", 10, "normal"), align='right')


s.update()
s.tracer(1)
