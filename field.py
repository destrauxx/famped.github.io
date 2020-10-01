import random
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
        chance = (2, 5, 7)
        for _ in range(user_number):
            rand_int = random.randrange(10)
            if rand_int in chance:
                    x_pol.append(['o'])
            else:
                    x_pol.append(['_']) 

    print('\nПоле после генерации')
    [print(f) for f in x_pol]
    return x_pol

def player_move(template, direction):
    if direction == 'right':
        for row in range(len(template)):
            for col in range(len(template)):
                if template[row][col] == 'x':
                    template[row][col] = '_'
                    template[row][col+1] = 'x'
                    return template
    if direction == 'left':
        for row in range(len(template)):
            for col in range(len(template)):
                if template[row][col] == 'x':
                    template[row][col] = '_'
                    template[row][col-1] = 'x'
                    return template
    if direction == 'up':
        for row in range(len(template)):
            for col in range(len(template)):
                if template[row][col] == 'x':
                    template[row][col] = '_'
                    template[row-1][col] = 'x'
                    return template
    if direction == 'down':
        for row in range(len(template)):
            for col in range(len(template)):
                if template[row][col] == 'x':
                    template[row][col] = '_'
                    template[row+1][col] = 'x'
                    return template
    return template
def save_load(direction, template):
    pass


def game():
    field_size = user_input_field()
    template = create_template(field_size)
    template[0][0] = 'x'

    print('\nПоле после добавление игрока на базовую позицию 0, 0')
    [print(f) for f in template]
        
    while True:
        usr_input = input('Укажите направление, exit для выхода, save сохранение, load загрузка: ')
        template = player_move(template, usr_input)
        if usr_input == 'exit':
            break
        [print(f) for f in template]

game()