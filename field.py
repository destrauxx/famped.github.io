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
    x_pol = []
    for u in range(user_number):
            x_pol.append('_' + ' ')
    return x_pol


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
    user_input_act = input('Для того чтобы перемещаться по полю использовать: up down right left и exit для выхода: ')
    return user_input_act


def the_character(act, x):
    '''
    input: act - act of user(str), x - x_pol(list)
    output: character coordinates(list)[x, y]
    '''
    coord = [0, 0]
    template = []
    x.pop([coord[1]][coord[0]])
    x.insert([coord[1]][coord[0]], 'x ')
    for i in range
    template.append(x)
    return template

def game():
    status = True
    field_size = user_input_field()
    while status:
        template = create_template(field_size)
        the_character(user_input_act, template)
        to_print = list_to_string_convert(the_character)

        for _ in range(field_size):
            print(to_print)

        user_act = user_input_act()

        if user_act == 'exit':
            status = False
        

game()