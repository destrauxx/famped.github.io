string = input('Введи любое слово, а я скажу - палиндром ли оно) ')

if string == string[::-1]:
    print(f'все ок, {string} это палиндром ')
else:
    print(f'{string} - не палиндром')