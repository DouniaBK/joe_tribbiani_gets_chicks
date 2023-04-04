
from pytimedinput import timedInput
import os
from random import randint
from colorama import Fore, init

""" 
setting the field's hight and width
setting the field's end zone and borders
"""
def print_field():
    for cell in CELLS:
        if cell in joes_body:
            print('🤵🏽', end='')
        elif cell[0] in (0, FIELD_WIDTH - 1) or cell[1] in (0, FIELD_HEIGHT - 1):
            print('🏿', end='')
        elif cell == chick_position:
            print('🐤', end='')
        else: 
            print(' ', end='')
        if cell[0] == FIELD_WIDTH - 1:
            print('')

            
"""
Move the snack by updating its position by giving the snack a new head and popping
the last element.
everytime the snake eats a chick, it gets larger by one cell
"""
def move_joe():
    global eaten

    new_head = joes_body[0][0] + direction[0], joes_body[0][1] + direction[1]
    joes_body.insert(0, new_head)
    if not eaten:
        joes_body.pop(-1)
    eaten = False
"""
check if the head of the snake is not in the same position than
the chick
if that is the case the chick should get a new position
if the snake eats the chick
"""
def chick_collision():
    global chick_position, eaten

    if chick_position[0] == joes_body:
        chick_position = new_position()
        eaten = True


"""
Place the chick in a new random position after being eaten
Make sure the new position is not on the border or
right where the snake is
"""
def new_position():
    col = randint(1, FIELD_WIDTH - 2)
    row = randint(1, FIELD_HEIGHT - 2)
    # the while loop is to make sure that the chick and snake are not in the same position
    while (col, row) in joes_body:
        col = randint(1, FIELD_WIDTH -2)
        row = randint(1, FIELD_HEIGHT -2)
    return (col, row)

init(autoreset=True)

# Field settings
FIELD_WIDTH = 32
FIELD_HEIGHT = 36
CELLS = [(col, row) for row in range(FIELD_HEIGHT) for col in range(FIELD_WIDTH)]


"""
The body of the snake a.k.a Joe (col, row // 2)
the body consists of three parts which are the three items in the list below
 the body moves towards the right
so the body (items 2 and 3) are the body positioned to the left behind the head
(item 1)
if the order is not from high to low the body will then crash into the head
"""
joes_body = [(5, FIELD_HEIGHT // 2),(4, FIELD_HEIGHT // 2),(3, FIELD_HEIGHT // 2)]
DIRECTIONS = {'left': (-1,0),'right': (1,0),'up': (0,-1,),'down': (0,1)}
#start of direction
direction = DIRECTIONS['right']
# The position of the chick or food
chick_position = new_position()
eaten = False
"""
limit the speed of the while loop to 0.3ms
run the game over and over until we break it with some command
without the while loop the game will only run once
"""
while True:
	# clear field
	os.system('cls')
	
	# draw field
	print_field()

	# get text that was entered and timed input
	txt,_ = timedInput('',timeout = 0.3)
    match txt:
        case 'w': direction = DIRECTIONS ['up']
        case 'a': direction = DIRECTIONS ['left']
        case 's': direction = DIRECTIONS ['down']
        case 'd': direction = DIRECTIONS ['right']
        case 'q':
            os.system('cls')
            break


    #update game elements position
    move_joe()
    chick_collision()

    #check death if snake crashes against the border or bites itself
    if joes_body[0][1] in (0, FIELD_WIDTH -1) or \
        joes_body[0][0] in (0, FIELD_HEIGHT -1) or \
        joes_body[0] in joes_body[1:]:
            os.system('cls')
            break

    


