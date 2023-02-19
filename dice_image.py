import turtle
s = turtle.Screen()

s.setup(700, 700)
s.tracer(0)

dice_area = turtle.Turtle()
dice_area.shape('circle')
dice_area.shapesize(0.01, 0.01, 0.01)
dice_area.color('white')

dice_area.penup()
dice_area.goto(0, 300)
dice_area.down()

dice_area.begin_fill()
dice_area.forward(25)
dice_area.right(90)
dice_area.forward(50)
dice_area.right(90)
dice_area.forward(50)
dice_area.right(90)
dice_area.forward(50)
dice_area.right(90)
dice_area.forward(25)
dice_area.end_fill()
s.update()
s.tracer(1)


"""
DOTS NUMERATION: the dots on the dice are counted sequentially from top left to bottom right
"""

s.tracer(0)

dot1 = turtle.Turtle()
dot1.shape('circle')
dot1.shapesize(0.5, 0.5, 0.5)
dot1.penup()
dot1.goto(-15, 290)
dot1.color('white')

dot2 = dot1.clone()
dot2.penup()
dot2.goto(15, 290)
dot2.color('white')

dot3 = dot1.clone()
dot3.penup()
dot3.goto(-15, 275)
dot3.color('white')

dot4 = dot1.clone()
dot4.penup()
dot4.goto(0, 275)
dot4.color('white')

dot5 = dot1.clone()
dot5.penup()
dot5.goto(15, 275)
dot5.color('white')

dot6 = dot1.clone()
dot6.penup()
dot6.goto(-15, 260)
dot6.color('white')

dot7 = dot1.clone()
dot7.penup()
dot7.goto(15, 260)
dot7.color('white')

s.update()
s.tracer(1)


def res_one():
    dot4.color('black')


def res_two():
    dot1.color('black')
    dot7.color('black')


def res_three():
    res_one()
    res_two()


def res_four():
    res_two()
    dot2.color('black')
    dot6.color('black')


def res_five():
    res_four()
    res_one()


def res_six():
    res_four()
    dot3.color('black')
    dot5.color('black')


def res_reset():
    dot1.color('white')
    dot2.color('white')
    dot3.color('white')
    dot4.color('white')
    dot5.color('white')
    dot6.color('white')
    dot7.color('white')
