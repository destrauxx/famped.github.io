def user_input_field():
    '''
    output: user_number(int)
    '''
    user_input_field = int(input('Укажи размер поля для игры: '))
    return user_input_field


def create_template(u):
    '''
    input: u - user_input_field(int)
    output: template
    '''
    user_number = u
    template = []
    for _ in range(user_number):
            template.append('_' + ' ')
    return template


def list_to_string_convert(t):
    """
    input: t - template (list)
    output: s - list converted to string
    """
    s = ''
    return s.join(t)


def user_input_act():
    '''
    output: act of user(str)
    '''
    user_input_act = input('Для того чтобы премещаться по полю использовать: up down right left и exit для выхода: ')
    return user_input_act


def the_character(act):
    '''
    input: act of user to replace character
    output: character coordinates(list)[x, y]
    '''
    coordinates = [0, 0]
    if act == 'up':
        coordinates[1] += 1
    elif act == 'down':
        coordinates[1] -= 1
    elif act == 'right':
        coordinates[0] += 1
    elif act == 'left':
        coordinates[0] -= 1
    return coordinates

def game():
    status = True
    field_size = user_input_field()
    while status:
        coordinats = the_character(user_input_act)
        template = create_template(field_size)
        to_print = list_to_string_convert(template)
        for f in range(field_size - 1):
            if coordinats[1] == f:
                print(to_print[1:coordinats[0]] + 'x ' + to_print[coordinats[0]:])
            print(to_print)
        user_act = user_input_act()
        if user_act == 'exit':
            break
        

game()