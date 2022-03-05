# В матрице найти среднее арифметическое элементов последних двух столбцов.
from random import randint

matrix = [[randint(0, 5) for i in range(3)] for j in range(3)]  # создание матрицы 3 на 3

result = 0  # переменная в которой будет хранится сумма элементов

for i in range(len(matrix)):  # перебор строк матрицы
    for j in range(-2, 0):  # перебор двух последних элементов каждой строки матрицы
        result += matrix[i][j]

print(*matrix, sep="\n")  # вывод исходной матрицы
print(f"Реузльтат: {result / (len(matrix) * 2)}")  # нахождение среднего арифметического
