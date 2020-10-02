from random import randint
#TODO:INPUT() LATER

user_input = 3

def build_field(size):
    """size int
    return list"""
    row = ['_'] * size
    col = []
    for _ in range(size): 
        col.append(row[:])
    return col

def mark_start_player(field):
    """field list
    return field list
    """
    field[0][0] = 'x'
    return field

f = mark_start_player(build_field(user_input))

def add_obstacles(field):
    '''field list
    return field list'''
    chance = 25
    for r in range(len(field)):
        for c in range(len(field)):
            if field[r][c] != 'x':
                r_num = randint(0, 100)
                if r_num <= chance:
                    field[r][c] = 'o'
    return field

add_obstacles(f)
print(f)