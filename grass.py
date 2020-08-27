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
    x_pol = []
    for u in range(user_number):
            x_pol.append('_' + ' ')
            template.append(x_pol)
    return x_pol, template


def list_to_string_convert(t):
    """
    input: t - template (list)
    output: s - list converted to string
    """
    s = ''
    return s.join(t[0])


def user_input_act():
    '''
    output: act of user(str)
    '''
    user_input_act = input('Для того чтобы перемещаться по полю использовать: up down right left и exit для выхода: ')
    return user_input_act


def the_character(act, stats, tmp):
    '''
    input: act - act of user(str), stats - status of while in game(bool), tmp - template(list)
    output: character coordinates(list)[x, y]
    '''
    coord = [0, 0]

    tmp.pop([coord[1]][coord[0]])
    tmp.insert([coord[1]][coord[0]], 'x ')
    return tmp

def game():
    status = True
    field_size = user_input_field()
    while status:
        template = create_template(field_size)
        the_character(user_input_act, status, template[1])
        to_print = list_to_string_convert(template)

        for _ in range(field_size):
            print(to_print)

        user_act = user_input_act()

        if user_act == 'exit':
            status = False
        

game()
