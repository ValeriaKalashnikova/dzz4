n = int(input('Введите количество элементов матрицы 1: '))
a = [int(i) for i in input('Введите элементы матрицы 1: ').split()]
m = int(input('Введите количество элементов матрицы 2: '))
b = [int(i) for i in input('Введите элементы матрицы 2: ').split()]
k = []
for i in a:
    if i in b and i not in k:
        k.append(i)
print(k)
