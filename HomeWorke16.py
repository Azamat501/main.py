N = abs(int(input('Введите количество элементов списка А:')))
A_entered = input ('Введите через пробел элементы списка:').split()
A_num = list(map(int, A_entered))
if len(A_num) != N:
    print('Введенные  элементы не сответствют заявленному количеству! ')
else:
    x = int(input('Введите чесло х. которое необходимо найти в списке :'))
    count = 0
    for i in range(N):
        if A_num[i] == x:
            count += 1
            print(f"чесло {x} встеречается в списке A {count} раз ")

