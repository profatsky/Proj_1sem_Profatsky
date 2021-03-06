# Вариант 19
# Дано целое число N (> 0). Найти сумму 1N + 2N-1 + ... + N1.
N = input('Введите целое положительное число: ')
result = 0
i = 1

# Обработка исключений
while type(N) != int:
    try:
        N = int(N)
        if N <= 0:
            print(f'Некорректный ввод - {N}!')
            N = input('Введите целое положительное число: ')
    except ValueError:
        print(f'Некорректный ввод - {N}!')
        N = input('Введите целое положительное число: ')

# Обработка чисел
while N >= 1:
    result += i ** N
    i += 1
    N -= 1

print(f'Сумма равна {result}\nПрограмма успешно завершена!')
