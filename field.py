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
            # x_pol.append('_' + ' ') - Зачем тут складывать две строки?
            x_pol.append(['_'] * user_number) # Создание горизонтальных полей с помощью умножения.

    #Выведем предварительный результат в консоль и убедимся, что код работает на этом моменте.
    print('\nПоле после генерации')
    [print(f) for f in x_pol]
    return x_pol

def player_move(template, direction):
    # Проверяем если напарвление движения -> направо
    if direction == 'right':
        # Проходим по нашему полю с помощью цикла, для поиска координат нашего персонажа
        for row in range(len(template)):
            for col in range(len(template)):
                # Если текущая ячейка содержит строку с персонажем
                if template[row][col] == 'x':
                    # Так как мы хотим двигаться направо
                    # x _ _       _ x _
                    # _ _ _   ->  _ _ _
                    # _ _ _       _ _ _
                    # Произошло банальное изменение индекса в колонке
                    template[row][col] = '_'
                    template[row][col+1] = 'x'
                    # Запусти этот код в анализаторе и посмотри, что будет без ключевого слова break
                    break
    if direction == 'left':
        # Проходим по нашему полю с помощью цикла, для поиска координат нашего персонажа
        for row in range(len(template)):
            for col in range(len(template)):
                # Если текущая ячейка содержит строку с персонажем
                if template[row][col] == 'x':
                    # Так как мы хотим двигаться направо
                    # x _ _       _ x _
                    # _ _ _   ->  _ _ _
                    # _ _ _       _ _ _
                    # Произошло банальное изменение индекса в колонке
                    template[row][col] = '_'
                    template[row][col-1] = 'x'
                    # Запусти этот код в анализаторе и посмотри, что будет без ключевого слова break
                    break
    if direction == 'up':
        # Проходим по нашему полю с помощью цикла, для поиска координат нашего персонажа
        for row in range(len(template)):
            for col in range(len(template)):
                # Если текущая ячейка содержит строку с персонажем
                if template[row][col] == 'x':
                    # Так как мы хотим двигаться направо
                    # x _ _       _ x _
                    # _ _ _   ->  _ _ _
                    # _ _ _       _ _ _
                    # Произошло банальное изменение индекса в колонке
                    template[row][col] = '_'
                    template[row+1][col] = 'x'
                    # Запусти этот код в анализаторе и посмотри, что будет без ключевого слова break
                    break
    if direction == 'down':
        # Проходим по нашему полю с помощью цикла, для поиска координат нашего персонажа
        for row in range(len(template)):
            for col in range(len(template)):
                # Если текущая ячейка содержит строку с персонажем
                if template[row][col] == 'x':
                    # Так как мы хотим двигаться направо
                    # x _ _       _ x _
                    # _ _ _   ->  _ _ _
                    # _ _ _       _ _ _
                    # Произошло банальное изменение индекса в колонке
                    template[row][col] = '_'
                    template[row-1][col] = 'x'
                    # Запусти этот код в анализаторе и посмотри, что будет без ключевого слова break
                    break
    return template

def game():
    status = True
    field_size = user_input_field()

    # Проверяем работоспособность текущих функций  
    template = create_template(field_size)
    
    # Если все работает как нам нужно, создаем базовое перемещение персонажа (например: направо)
    # Для этого укажем базовую позицию игрока (например: слева-сверху)
    template[0][0] = 'x'

    # Обязательно проверяем на этот моменте, работоспособность
    print('\nПоле после добавление игрока на базовую позицию 0, 0')
    [print(f) for f in template]
        
    # Создадим базовую функцию приема пользовательского ввода
    #TODO Если все будет работать переделать на - usr_input = input('Укажите направление')
    usr_input = input('Укажите направление из right left up down')

    # Создадим базовый функционал перемещения с помощью функции player_move(template, direction)
    template = player_move(template, usr_input)

    # Обязательно проверяем на этот моменте, работоспособность
    print('\nПоле после перемещения игрока на один индекс вправо 0, 1')
    [print(f) for f in template]

game()