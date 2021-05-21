for t in reversed(range(4)):
    n = input('Введите логин: ')
    p = input('Введите пароль: ')
    if n == 'влад' and p == '12345':
        print('Ok')
        break
    if t > 0:
        print('Осталось', t, 'попытки!')
else:
    print('В доступе отказано!')
