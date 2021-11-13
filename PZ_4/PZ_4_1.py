# Вариант 19
# Дано вещественное число X и целое число N (> 0).
# Найти значение выражения X - X3/(3!) + X5/(5!) - ... + (-1) ** N * X ** (2 * N+1) /((2 * N+1)!) (N! = 12 ...N).
# Полученное число является приближенным значением функции sin в точке X.

# Функция для нахождения факториала
def get_factorial(num):
    factorial = 1
    while num >= 1:
        factorial *= num
        num -= 1
    return factorial


X = input('Введите число: ')
N = input('Введите целое положительное число: ')
i = 1
sign = 0
result = 0

# Обработка исключений
while type(X) != float:
    try:
        X = float(X)
    except ValueError:
        print(f'Некорректный ввод - {X}!')
        X = input('Введите число: ')

while type(N) != int:
    try:
        N = int(N)
        if N <= 0:
            print(f'Некорректный ввод - {N}!')
            N = input('Введите целое положительное число: ')
    except ValueError:
        print(f'Некорректный ввод - {N}!')
        N = input('Введите целое положительное число: ')


# Нахождение значения выражения
while i < 2 * N + 1:
    result += (-1) ** sign * X ** i / get_factorial(i)
    i += 2
    sign += 1

print(f'Значение выражения равно {result + (-1) ** N * X ** (2 * N + 1) / get_factorial(2 * N + 1)}')
print('Программа успешно завершена!')