# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

N = int(input('Введите длину массива: '))
A = input('Введите элементы массива через пробел ').split()
arr = list(map(int, A))

if len(arr) != N or N == 0:
    print('Введенные элементы не соответствуют заявленному количеству')
else:
    print (arr)
    X = int(input('Введите искомое число: '))
    count = 0
    for i in range(N):
        if arr[i] == X:
            count += 1
    print('Данное число встречается ', count, 'раз')
