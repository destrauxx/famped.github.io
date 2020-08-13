def user_input():
    '''
    input: -
    output: user_input(int)
    '''
    user_input = int(input('Введи число этажей у пирамиды:'))
    return user_input

def check_ui_parity(un):
    '''
    input: un - user_number(int)
    output: bool, if un parity - print about this and return True
    '''
    if un % 2 == 0:
        print('Нужно ввести нечетное число')
        return True
def function():
    user_number = user_input()
    floor = '*'
 
    for l in range(1, user_number + 1):
        if check_ui_parity(user_number):
            break
        
        if user_number / 2 != l:
            print(floor*l)
            

        

function()