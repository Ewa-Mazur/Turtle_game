import turtle

s = turtle.Screen()
s.setup(700, 700)


def buttons():
    # creating objects

    info = turtle.Turtle()
    info.shape('circle')
    info.shapesize(0.01, 0.01, 0.01)

    global match_result
    match_result = turtle.Turtle()
    match_result.shape('circle')
    match_result.shapesize(0.01, 0.01, 0.01)

    # positions settings
    s.tracer(0)

    info.penup()
    info.goto(50, 220)
    info.write('Click red button to roll the dice!', font=("Verdana", 10, "normal"), align='left')

    match_result.penup()
    match_result.goto(0, -300)

    mask_button = turtle.Turtle()
    mask_button.shape('circle')
    mask_button.shapesize(1, 1, 1)
    mask_button.fillcolor('grey')
    mask_button.penup()
    mask_button.goto(0, 230)

    global roll_button
    roll_button = turtle.Turtle()
    roll_button.shape('circle')
    roll_button.shapesize(1, 1, 1)
    roll_button.fillcolor('red')
    roll_button.penup()
    roll_button.goto(0, 230)


    s.update()


buttons()
