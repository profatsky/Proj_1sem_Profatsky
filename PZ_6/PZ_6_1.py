# Вариант 19
# Дан список размера N и целые числа K и L (1 < K < L < N). Найти сумму элементов списка с номерами от K до L
# включительно.
from random import randint

# Ввод данных
while True:
    N, K, L = int(input('Введите размер списка: ')), int(input('Введите первое число: ')), \
              int(input('Введите второе число: '))
    if 1 < K < L < N:
        break
    print('Не соблюдено условие 1 < K < L < N')

# Генерация списка
my_list = [randint(1, 9) for i in range(N)]

k = 0

# Ищем сумму
for i in my_list[K:L+1]:
    k += i

print(f'Список - {my_list}. Сумма - {k}')
