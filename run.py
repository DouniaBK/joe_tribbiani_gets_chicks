
""" 
setting the field's hight and width
setting the field's end zone and borders
"""


def print_field():
    for cell in CELLS:
        if cell in joes_body:
            print('X', end='')

        elif cell[0] in (0, FIELD_WIDTH - 1) or cell[1] in (0, FIELD_HEIGHT - 1):
            print('🏿', end='')
        elif cell == chick_position:
            print('🐤', end='')
        else: 
            print(' ', end='')
        if cell[0] == FIELD_WIDTH - 1:
            print('')


FIELD_WIDTH = 32
FIELD_HEIGHT = 36
CELLS = [(col, row) for row in range(FIELD_HEIGHT) for col in range(FIELD_WIDTH)]


# The position of the chick
chick_position = (5, 10)
"""
The body of the snake a.k.a Joe (col, row // 2)
the body is here three tuples where the body moves towards the right
so the body (here tuple 2 and 3) are the body meaning to the left behind the head
which is tuple 1
if the order is not from high to low the body will then crash with the head
"""
joes_body = [(5, FIELD_HEIGHT // 2), (4, FIELD_HEIGHT // 2), (3, FIELD_HEIGHT //2)]
print_field()


