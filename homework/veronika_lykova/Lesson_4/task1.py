my_dict = {
    'tuple': (256, 6.66, None, 'aqua', True),
    'list': [128, None, 'terra', False, 9.999, 'air'],
    'dict': {'one': 1, 'two': 'two', 'three': True, 'four': 'human', 'five': 5.25},
    'set': {222, None, 'nature', False, 222, 21, False}
}

# Для того, что хранится под ключом ‘tuple’:
# выведите на экран последний элемент
print(my_dict['tuple'][-1])

# Для того, что хранится под ключом ‘list’:
# добавьте в конец списка еще один элемент
# удалите второй элемент списка
my_dict['list'].append('new element')
my_dict['list'].pop(1)

# Для того, что хранится под ключом ‘dict’:
# добавьте элемент с ключом ('i am a tuple',) и любым значением
# удалите какой-нибудь элемент
my_dict['dict'][('i am a tuple',)] = 'value for the new key'
my_dict['dict'].pop('one')

# Для того, что хранится под ключом ‘set’:
# добавьте новый элемент в множество
# удалите элемент из множества
my_dict['set'].add('new shiny element')
my_dict['set'].pop()

print(my_dict)
