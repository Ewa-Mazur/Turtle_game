import turtle
import random
import time

turtle.title("Racing turtle")

s = turtle.Screen()
s.setup(700,700)

#creating objects

info = turtle.Turtle()
info.shape('circle')
info.shapesize(0.01,0.01,0.01)

exit_button = turtle.Turtle()
exit_button.shape('square')
exit_button.shapesize(0.5,0.5,1)

match_result = turtle.Turtle()
match_result.shape('circle')
match_result.shapesize(0.01,0.01,0.01)

#positions settings
s.tracer(0)

exit_button.penup()
exit_button.goto(320,320)
exit_button.write('EXIT\n', font=("Verdana", 7, "normal"), align='center')

info.penup()
info.goto(50,220)
info.write('Click red button to roll the dice!', font=("Verdana", 10, "normal"), align='left')

match_result.penup()
match_result.goto(0,-300)

roll_button = turtle.Turtle()
roll_button.shape('circle')
roll_button.shapesize(1,1,1)
roll_button.fillcolor('red')
roll_button.penup()
roll_button.goto(0,230)

s.update()

def exit(x,y):
    s.bye()

exit_button.onclick(exit)


