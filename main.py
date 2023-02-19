import turtle
import background
import buttons
import dice_image
import random


turtle.title("Racing turtle")
s = turtle.Screen()
s.setup(700,700)


#turtle setup, step size setup

t1 = turtle.Turtle()
t1.fillcolor("red")
t1.shape("turtle")
t1.shapesize(3,3,3)

t2 = turtle.Turtle()
t2.fillcolor("green")
t2.shape("turtle")
t2.shapesize(3,3,3)


step_size = 20


def turtle_starting_pos():
    s.tracer(0)
    t1.clear()
    t1.penup()
    t1.goto(-300,100)
    t1.pendown()

    t2.clear()
    t2.penup()
    t2.goto(-300,-100)
    t2.pendown()
    s.update()
    s.tracer(1)
    
    buttons.match_result.clear()
  

turtle_starting_pos()

#players names input

player1 = s.textinput("Player 1", "Name of first player:")
player2 = s.textinput("Player 2", "Name of second player:")

if player1:
    if player1 == "":
        player1 = "Red turtle"
    player1 = player1.capitalize()
else:
    player1 = "Red turtle"

if player2:
    if player2 == "":
        player2 = "Green turtle"
    player2 = player2.capitalize()
else:
    player2 = "Green turtle"


#movements

dice_results = []
dice_dict = {
    '1':dice_image.res_one,
    '2':dice_image.res_two,
    '3':dice_image.res_three,
    '4':dice_image.res_four,
    '5':dice_image.res_five,
    '6':dice_image.res_six
    }

def dice_result(x,y):
    
    dice_image.res_reset()
    
    result = str(random.choice([1,2,3,4,5,6]))
    dice_dict[result]()
    
    s.listen()
    dice_results.append(result)
    

    if len(dice_results) %2 != 0:
        t1.fd(int(result)*step_size)

    elif len(dice_results) %2 ==0:
        t2.fd(int(result)*step_size)

    
    #winner information
    if t1.pos() >= (250,100):
        buttons.match_result.write(player1+' wins!', font=("Verdana", 20, "normal"), align='center')

    if t2.pos() >= (250,-100):
        buttons.match_result.write(player2+' wins!', font=("Verdana", 20, "normal"), align='center')

    #replay option
    if t1.pos() >= (250,100) or t2.pos() >= (250,-100):
        replay = s.textinput("Play again?", "Type 'Y' to play again, type 'N' to exit")


        if replay:
            if replay in {'y','Y'}:
                turtle_starting_pos()
            elif replay.capitalize()=='N':
                s.bye()
            else:
                while replay not in {'Y','y','N','n'}:
                    replay = s.textinput("I don't understand...", "Type 'Y' to play again, type 'N' to exit")
                    if replay.capitalize()=='Y':
                        turtle_starting_pos()
                        dice_image.res_reset()
                    elif replay.capitalize()=='N':
                        s.bye()
        elif replay =='':
            turtle_starting_pos()
            dice_image.res_reset()
        else:
            s.bye()

 
#rolling the dice and making the turtules to move - calling fun 'dice_result' on click
buttons.roll_button.onclick(dice_result)

turtle.done()

