# Вариант 19
# Проверить истинность высказывания: "Среди трех данных целых чисел есть хотя бы одна пара совпадающих".

# Обработка исключений
def exception_handing(num):
    while type(num) != int:
        try:
            num = int(num)
        except ValueError:
            print(f'Некорректный ввод - {num}!')
            num = input('Введите новое целое число вместо этого: ')
        else:
            return num


a, b, c = input('Введите первое целое число: '), input('Введите второе целое число: '), input('Введите третье целое '
                                                                                              'число: ')

a = exception_handing(a)
b = exception_handing(b)
c = exception_handing(c)

# Проверка истинности высказывания
if a == b or a == c or a == b == c or b == c:
    print('Среди трех данных чисел есть как минимум одна пара совпадающих')
else:
    print('Среди трех данных числе нет ни одной пары совпадающих')
print('Программа успешно завершена!')
