
""" 
setting the field's hight and width
setting the field's end zone
"""
def print_field():
   for cell in CELLS:
    print(cell)

FIELD_WIDTH = 32
FIELD_HEIGHT = 36
CELLS = [(col,row) for row in range(FIELD_HEIGHT) for col in range(FIELD_WIDTH)]

print_field()


