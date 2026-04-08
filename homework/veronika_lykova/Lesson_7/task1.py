a = 56
while True:
    user_input = int(input('Угадайте цифру: '))
    if user_input != a:
        print('Попробуйте снова')
    else:
        print('Поздравляю! Вы угадали!')
        break
