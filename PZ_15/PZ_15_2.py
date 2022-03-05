# Перенести в новую матрицу Matr1 элементы, которые не находятся в первых и последних строках и столбцах
# матрицы Matr2 произвольного размера.
from random import randint

n = int(input("Введите размерность квадратной матрицы (целое число): "))

matr2 = [[randint(0, 5) for i in range(n)] for j in range(n)]  # создание матрицы 5 на 5

# Создание новой матрицы с нужными элементами
matr1 = []
for i in range(len(matr2)):
    temp = []
    for j in range(len(matr2[0])):
        # проверка, не находится ли элемент в неподходящих столбцах или строках
        if i not in (0, len(matr2) - 1) and j not in (0, len(matr2[0]) - 1):
            temp.append(matr2[i][j])
    if temp:
        matr1.append(temp)

print("matr2: ", *matr2, "matr1: ", *matr1, sep='\n')  # вывод результа
