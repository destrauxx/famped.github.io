phrase = 'Fair is foul, and foul is fair: Hover through the fog and filthy air.'
lower_letters = 0
upper_letters = 0

print(phrase)
def lower_case(p, l):
    '''
    input - p - phrase(str), l - lower_letters(int)
    output - how in phrase lower letters
    '''
    for i in p:
        if i == i.lower() and i != ' ' and i != ',' and i != '.' and i != ':':
            l = l + 1
    print(f'Total lowercase letters in sentence is: {l}')
def upper_case(p, u):
    '''
    input - p - phrase(str), u - upper_letters(int)
    output - how in phrase upper letters
    '''
    for i in p:
        if i == i.upper() and i != ' ' and i != ',' and i != '.' and i != ':':
            u = u + 1
    print(f'Total uppercase letters in sentence is: {u}')

lower_case(phrase, lower_letters)
upper_case(phrase, upper_letters)



