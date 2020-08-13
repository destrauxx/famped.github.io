phrase = 'Fair is foul, and foul is fair: Hover through the fog and filthy air.'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
lower_letters = 0
upper_letters = 0

print(phrase)
# def lower_case(p, l):
#     '''
#     input - p - phrase(str), l - lower_letters(int)
#     output - how in phrase lower letters
#     '''
#     for i in p:
#         if i == i.lower() and i != ' ' and i != ',' and i != '.' and i != ':':
#             l = l + 1
#     print(f'Total lowercase letters in sentence is: {l}')
    
def lower_case(p):
    '''
    input: p - phrase(str)
    output: tmp, count of lower letters in p
    '''
    tmp = 0
    for i in p:
        for a in alphabet:
            if i == a.lower():
                tmp += 1
    return tmp

def upper_case(p, u):
    '''
    input - p - phrase(str), u - upper_letters(int)
    output - how in phrase upper letters
    '''
    for i in p:
        if i == i.upper() and i != ' ' and i != ',' and i != '.' and i != ':':
            u = u + 1
    print(f'Total uppercase letters in sentence is: {u}')

lower_letters = lower_case(phrase)
upper_case(phrase, upper_letters)

print(lower_letters)



