# Вариант 19
# Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из результата вновь вычли сумму его цифр
# и т.д. Через сколько таких действий получтся нуль?

# Объявление функции по обработке чисел
def solution(num):
    total = 0
    while num > 0:
        total += num % 10
        num = num // 10
    return total


# Ввод данных
a = input('Введите число: ')
k = 0

# Обработка исключений
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print(f'Некорректный ввод - {a}!')
        a = input('Введите новое целое число вместо этого: ')


# Обработка чисел
while a > 0:
    a -= solution(a)
    k += 1

print(k)
