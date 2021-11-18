# Вариант 19
# Дан целочисленный спиоск размера N. Найти количество различных элементов в данном списке
from random import randint

# Ввод данных
N = int(input('Введите размер списка: '))

# Генерация списка
my_list = [randint(1, 9) for i in range(N)]

# Ищем количество различных элементов списка
amount = 0
for i in range(N):
    if my_list[i] not in my_list[:i]:
        amount += 1

print(f'В списке {my_list} есть {amount} различных элементов')
