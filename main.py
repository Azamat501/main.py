num = input('Введите 3-х значное число: ')
res = 0
if len(num) == 3:
    for i in num:
        res += int(i)
    print(res)
else:
    print('Вы ввели не 3-х значное число')