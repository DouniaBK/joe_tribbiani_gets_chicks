
from pytimedinput import timedInput
import os
from random import randint

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
"""
def move_joe():
    new_head = joes_body[0][0] + direction[0], joes_body[0][1] + direction[1]
    joes_body.insert(0, new_head)
    joes_body.pop(-1)


def chick_collision():
    global chick_position, eaten

    if chick_position[0] == joes_body:
        chick_position = new_position()
        eaten = True


def new_position():
    col = randint(1, FIELD_WIDTH - 2)
    row = randint(1, FIELD_HEIGHT - 2)
    while (col, row) in joes_body:
        col = randint(1, FIELD_WIDTH -2)
        row = randint(1, FIELD_HEIGHT -2)
    return (col, row)

# Field settings
FIELD_WIDTH = 32
FIELD_HEIGHT = 36
CELLS = [(col, row) for row in range(FIELD_HEIGHT) for col in range(FIELD_WIDTH)]


"""
The body of the snake a.k.a Joe (col, row // 2)
the body consists of three parts which are the three items in the list below
 the body moves towards the right
so the body (here tuple 2 and 3) are the body meaning to the left behind the head
which is tuple 1
if the order is not from high to low the body will then crash with the head
"""
joes_body = [(5, FIELD_HEIGHT // 2),(4, FIELD_HEIGHT // 2),(3, FIELD_HEIGHT // 2)]
DIRECTIONS = {'left': (-1,0),'right': (1,0),'up': (0,-1,),'down': (0,1)}
#start of direction
direction = DIRECTIONS['right']
# The position of the chick or food
chick_position = new_position()

"""
limit the speed of the while loop to 0.3ms
run the game over and over until we break it with some command
without the while loop the game will only run once
"""
while True:
    # clear field in terminal
	os.system('cls')


    # draw the game field
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
    


