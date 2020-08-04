print('''Добро пожаловать в игру - hangman 2000
    Ваша задача угадать загаданное слово за несколько попыток,
    иначе вас ждет расплата!
    Загаданное слово состоит из 6 букв ______ ''')

game_word = list("orange")          
game_status = list("______")
game_attempts = 3

def game():
    global game_attempts
    for l in range(len(game_word) + game_attempts):
        user_input = input("Введите букву:  ")
        for i in range(len(game_word)):
            if user_input in game_word[i]:
                game_status.pop(i)
                game_status.insert(i, user_input)
        if user_input not in game_word:
            game_attempts -= 1
            print(f'Осталось {game_attempts} попыток!')
        if  game_status == game_word:      
            print('Поздравляю, ты победил!')
            break
        elif game_attempts == 0:
            print('Ты проиграл')
            break
        print(f'Результат:  {game_status}')
        
            
        
        
           
        
game()




