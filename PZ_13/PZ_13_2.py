# Вариант 19
# Составить генератор (yield), который преобразует все буквенные символы в заглавные

# Функция с ключевым словом yield, которая преобразует все буквенные символы в заглавные
def func_generator(input_lst):
    for i in input_lst:
        if type(i) == str:
            i = i.upper()
        yield i


lst = [1, "hello", True, 2, "world!"]  # входные данные (список элементов с разными типами данных)
output = []  # список output, в который будет записан результат
my_generator = func_generator(lst)  # создаем генератор

# Добавляем элементы, которые возвращает yield, в список output
for j in my_generator:
    output.append(j)

print(output)  # вывод результата
