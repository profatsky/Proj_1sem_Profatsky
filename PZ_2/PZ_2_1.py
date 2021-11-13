# Вариант 19
# Дано трехзначное число. В нем зачеркнули первую справа цифру и приписали ее слева. Вывести полученное число.
a = input('Введите целое трехзначное число: ')

# Обработка исключений
while type(a) != int:
    try:
        a = int(a)
        if not 100 <= a <= 999:
            print('Некорректный ввод!')
            a = input('Введите целое трехзначное число: ')
    except ValueError:
        print('Некорректный ввод!')
        a = input('Введите целое трехзначное число: ')

# Обработка чисел
b = a % 10
a = a // 10

print(str(b) + str(a))
print('Программа успешно завершена!')