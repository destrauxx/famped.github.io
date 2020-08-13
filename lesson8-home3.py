def user_input():
    '''
    input: -
    output: user_input(int)
    '''
    user_input = int(input('Введи число: '))
    return user_input

def func():
    '''
    input: -
    output: number pattern, for example:
                                ui == 5
                                1
                                22
                                333
                                4444
                                55555
    '''
    user_number = user_input()
    for l in range(1, user_number + 1):  #Since the loop starts from 0, and we need to output from 1, the beginning of the list and the end are moved 1 position
        print(f'{l}'*l)

func()