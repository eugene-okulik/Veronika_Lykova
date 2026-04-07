string1 = 'результат операции: 42'
string2 = 'результат операции: 514'
string3 = 'результат работы программы: 9'
string4 = 'результат: 2'


def plus_ten(string):
    find_number_position = string.index(':') + 2
    number = int(string[find_number_position:]) + 10
    print(number)


plus_ten(string1)
plus_ten(string2)
plus_ten(string3)
plus_ten(string4)
