mage_name = input('Введи имя мага: ')
druid_name = input("Введи имя друида: ")

class Pers():
    def attack(self, name):
        print(f'{name} аттакует')

while True:
    attack_name = input('Выбери аттакующего(маг или друид): ').lower()
    pers = Pers()
    if attack_name == 'маг':
        pers.attack(name=f'{mage_name}')
    elif attack_name == 'друид':
        pers.attack(name=f'{druid_name}')
    else:
        print('Нет такого, промах и провал, сударь!')


    