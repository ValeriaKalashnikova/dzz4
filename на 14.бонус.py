n = int(input('Введите количество элементов матрицы: '))
a = [int(i) for i in input('Введите элементы матрицы: ').split()]
imin = min(a)
delta = int(input('Введите дельта: '))
k=0
for j in a:
    if (j - imin) == delta:
        k+=1
print(k)
