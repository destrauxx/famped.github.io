# VERSION ONE
# ДЛЯ переключения между вариантами ЗАКОММЕНТИРОВАТЬ НЕ используемый вариант
string = input('Введи строку, а я ее переверну! ')
def string_back(st):
    '''
        Ввод : st --> строка
        Вывод : st --> перевернутая строка
    '''
    return st[::-1]

print(string_back(string))

# VERSION TWO
# string = input('Введи строку, а я ее переверну! ')

# def string_back(st):
#     '''
#         Ввод : st --> строка
#         Вывод : st --> перевернутая строка
#     '''
#     for l in range(string, 0, -1):
