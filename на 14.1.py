n = int(input('Введите количество элементов матрицы: '))
array = [float(i) for i in input('Введите элементы матрицы: ').split()]
imax = 0
indexmax = 0
for i in range(n):
    if (array[i] > imax):
        imax = array[i]
        indexmax = i
for j in range(indexmax + 1, n):
    array[j] = 0
print(array)