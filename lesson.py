# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"Cat: {self.name}"


# fluffy = Cat("fluffy")

# print(fluffy)



# class Foo():
#     def __init__(self, number):
#         self.number = number

#     def __str__(self):
#         return f"Foo: {self.number}"

#     def __add__(self, other):
#         result = self.number - other.number
#         return Foo(result)

# a = Foo(5)
# b = Foo(17)

# c = a + b
# print(c)


# class Franction:
#     def __init__(self, numer, denom):
#         self.numer = numer
#         self.denom = denom

#     def __str__(self):
#         return f'{self.numer} / {self.denom}'

#     def get_numer(self):
#         return self.numer

#     def get_denom(self):
#         return self.denom
    
#     def __add__(self, other):
#         result_numer = self.numer * other.denom + other.numer * self.denom
#         result_denom = self.denom * other.denom

#         return Franction(result_numer, result_denom)
    
#     def __sub__(self, other):
#         result_numer = self.numer * other.denom - other.numer * self.denom
#         result_denom = self.denom * other.denom

#         return Franction(result_numer, result_denom)

#     def convert(self):
#         return self.numer / self.denom


# oneHalf = Franction(1, 2)
# forty = Franction(1, 4)
# print(forty.convert())


from random import randint

class Potion:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality

    def __str__(self):
        return f'This potion named: {self.name}'

    def get_quality(self):
        return self.quality

    def get_name(self):
        return self.name

    def __add__(self, other):
        self_len = len(self.name) // 2
        other_len = len(other.name) // 2
        new_name = self.name[:self_len] + other.name[other_len:]
        quality = (self.quality + other.quality) / 2

        return Potion(new_name, quality)

    def __sub__(self, other):
        quality = self.quality - other.quality
        
    
        return Potion(self.name, quality)

    def check_quality(self):
        if self.quality > 75:
            print('ХАРОШАЯ РАБОТА, АЛЕК')
        elif self.quality > 50:
            print('НЕПЛОХАЯ РАБОТА ДИМАС')
        else:
            print('АЛЕЖА, ВСЕ *****, ПЕРЕДЕЛЫВАЙ')
game = True
while game:
    potion = input('Зелье : к - качественное, н - не качественное')
    if potion == 'exit':
        game = False
    else:
        potion_name = input('Название зелья')
        potion_quality = randint(1, 100)
        if potion == 'к':
            new_potion = QualityPotion(potion_name, potion_quality)
        else:
            new_potion = NotQualityPotion(potion_name, potion_quality)
        potions[potion_name] = new_potion
