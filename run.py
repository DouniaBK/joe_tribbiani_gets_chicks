
""" 
setting the field's hight and width
setting the field's end zone and borders
"""


def print_field():
    for cell in CELLS:
        if cell[0] in (0, FIELD_WIDTH - 1) or cell[1] in (0, FIELD_HEIGHT - 1):
            print('#', end='')
        else: 
            print(' ', end='')
        if cell[0] == FIELD_HEIGHT - 1:
            print('')


FIELD_WIDTH = 32
FIELD_HEIGHT = 36
CELLS = [(col, row) for row in range(FIELD_HEIGHT) for col in range(FIELD_WIDTH)]

print_field()


