# Вариант 19
# Описать функцию ShiftLeft3(A, B, C), выполняющую левый циклический сдвиг: значение A переходит в C, значение C - в B,
# значение B - в А (А, B, C - вещественные параметры, являющиеся одновременно выходными и выходными). С помощью этой
# функции выполнить левый циклический сдвиг для двух данных наборов из трех чисел: (A1, B1, C1) и (A2, B2, C2)

# Обработка исключений
def exception_handing(num):
    while type(num) != float:
        try:
            num = float(num)
        except ValueError:
            print(f'Некорректный ввод - {num}!')
            num = input('Введите новое число вместо этого: ')
        else:
            return num


# Объявление функции по обаботке чисел
def shift_left_3(first, second, third):
    first, second, third = second, third, first
    return first, second, third


# Ввод данных
A1, B1, C1 = input('Введите первое число первого набора: '), input('Введите второе число первого набора:'), \
             input('Введите третье число первого набора: ')

A2, B2, C2 = input('Введите первое число второго набора: '), input('Введите второе число второго набора:'), \
             input('Введите третье число второго набора: ')

A1 = exception_handing(A1)
B1 = exception_handing(B1)
C1 = exception_handing(C1)
A2 = exception_handing(A2)
B2 = exception_handing(B2)
C2 = exception_handing(C2)

# Обработа и вывод чисел
print(f'Первый набор после обработки: {shift_left_3(A1, B1, C1)}')
print(f'Второй набор после обработки: {shift_left_3(A2, B2, C2)}')
