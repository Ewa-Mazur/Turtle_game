import turtle
import background
import buttons
import dice_image
import random

turtle.title("Racing turtle")
s = turtle.Screen()
s.setup(700, 700)

step_size = 20
players_names = []
# turtle starting position Y coordinates
x = [0, -75, 75, -150, 150]


dice_results = []
dice_dict = {
    '1': dice_image.res_one,
    '2': dice_image.res_two,
    '3': dice_image.res_three,
    '4': dice_image.res_four,
    '5': dice_image.res_five,
    '6': dice_image.res_six
    }

color_dict = {
    'b': 'black',
    'g': 'green',
    'p': 'pink',
    'r': 'red',
    'y': 'yellow',
    'o': '#fabd2f'
    }

colors_list = ['b', 'B', 'g', 'G', 'p', 'P', 'r', 'R', 'y', 'Y', 'o', 'O']

def turtle_starting_pos(i):
    s.tracer(0)
    num[i].clear()
    num[i].shape("turtle")
    num[i].shapesize(3, 3, 3)
    num[i].penup()
    num[i].goto(-300, x[i])
    num[i].pendown()
    s.update()
    s.tracer(1) 

def players_settings():
    global players_dict
    global num
    global number_of_players
    num = []

    s.tracer(0)
    
    number_of_players = s.textinput("Number of players", "Enter number of players: 1-5")

    while number_of_players not in {'1', '2', '3', '4', '5'}:
        number_of_players = s.textinput("Number of players", "Enter CORRECT NUMBER of players: 1-5")
        if number_of_players in {'1', '2', '3', '4', '5'}:
            break
    number_of_players = int(number_of_players)
        
    for i in range(0, number_of_players):
        player_name = s.textinput("Player "+str(i+1), "Name of the " +str(i+1)+" player:")

        if player_name:
            if player_name == "":
                players_names.append('Anonymous_'+str(i))
            else:
                players_names.append(player_name.capitalize())
        else:
            players_names.append('Anonymous_'+str(i))

        num.append(turtle.Turtle())

        color = s.textinput(players_names[i]+", choose color!", "Enter letter:\n\nb - black \ng - green \np - pink"
                                                                    " \nr - red \ny - yellow \no - orange\n")
        while color not in colors_list:
            color = s.textinput(players_names[i]+", choose color!", "Enter correct letter:\n\nb - black \ng - green"
                                                                        " \np - pink \nr - red \ny - yellow "
                                                                        "\no - orange\n")
            if color in colors_list:
                break

        num[i].fillcolor(color_dict[color.lower()])        
        turtle_starting_pos(i)
   

       

def rematch_settings():
    dice_image.res_reset()
    buttons.match_result.clear()  
    
    for i in range(number_of_players):
        turtle_starting_pos(i)
            

def dice_result(_, __):

    dice_image.res_reset()
    buttons.roll_button.hideturtle()
    
    result = str(random.choice([1, 2, 3, 4, 5, 6]))
    dice_dict[result]()
    
    s.listen()
    dice_results.append(result)


    player_turn = len(dice_results) % number_of_players
    if player_turn == 0:
        player_turn = number_of_players

    num[player_turn-1].fd(int(result)*step_size)

    buttons.roll_button.showturtle()

    

    for i in range(number_of_players):
        if num[i].xcor() >= 250:
            buttons.match_result.write(str(players_names[i])+' wins!', font=("Verdana", 20, "normal"), align='center')
            replay()

        

def replay():
    replay = s.textinput("Play again?", "Type 'Y' to play again, type 'N' to exit")

    if replay:
        replay = replay.capitalize()
        if replay == 'Y':
            rematch_settings()
                    
        elif replay == 'N':
            s.bye()
        else:
            while replay not in {'Y', 'N'}:
                replay = s.textinput("I don't understand...", "Type 'Y' to play again, type 'N' to exit")
                replay = replay.capitalize()
                if replay == 'Y':
                    rematch_settings()
                elif replay == 'N':
                    s.bye()
    elif replay == '':
        rematch_settings()
    else:
        s.bye()   


players_settings()
buttons.roll_button.onclick(dice_result)

turtle.done()
