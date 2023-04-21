N = abs(int(input("Введите количество элементов списка А:")))
A_entered = input("Введите через пробел элементы списка: ")
A_num = list(map(int, A_entered))
if len(A_num) != N or N == 0:
    print("Введеные элемент не соответсвуют заявленному колиеству! ")
else:
    X = int(input("Введите число Х, с которого необходимо сравнить элементы списка: "))
    min = abs(X - A_num[0])
    index = 0
    for i in range(1, N):
        count = abs(x - A_num[i])
        if count < min:
            min = count
            index = i
            print(f"чесло {A_num[index]} в списке A наиболе близко по велечине к чеслу {x}, их разница составляет {abs(x - A_num[index])}")

