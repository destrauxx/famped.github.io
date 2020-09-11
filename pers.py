name = input('Имя: ')
_class = input('Класс- актер, ведущий, гость: ')
number = input('Шоу- шокеры, красная комната, суфлер, меняй: ')
guest = input('Гость- с, без: ')

pers = {f'{name}': {f'{_class}': {'number': f'{number}', 'guest': f'{guest}'}}}
print(pers)