print('За одну пиццу 500')
visitors = int(input('Сколько человек придет? '))
money = int(input('Сколько деняг есть? '))
pizza = int(money / 500)

if pizza < 1:
   print('У тя нема денег(')
elif pizza < 2:
    print('Это только на одну');
elif visitors > pizza * 2:
    print(f'К сожалению, вам {pizza} пиццы не хватит')
elif pizza >= visitors * 4:
    print(f'Пиццы многовато для {visitors} человек')
elif pizza >= 2 :
    print(f'Для {visitors} человек, как раз {int(pizza)} пиццы')

