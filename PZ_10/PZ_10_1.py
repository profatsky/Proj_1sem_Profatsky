# Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и
# отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив трбуемую
# обработку элементов: исходные данные, количество элементов, сумма элементов, элементы до n-1 умноженные на n
from random import randint

# Генерация первого текстового файла с исходныи данными
with open('text1_PZ_10_1.txt', 'w', encoding='UTF-8') as inp:
    seq = " ".join([str(randint(-10, 10)) for i in range(10)])
    seq = seq.replace('0', '1')
    inp.writelines(seq)

# Генерация второго текстового файла
with open('text1_PZ_10_1.txt', 'r', encoding='UTF-8') as inp:  # открываем первый файл на чтение
    input_text = inp.read()
    with open('text2_PZ_10_1.txt', 'w', encoding='UTF-8') as f:  # генерируем второй файл на запись
        # Записываем строку с исходными данными
        f.writelines(f'Исходные данные: {input_text}\n')
        # Записываем строку с количеством элементов
        f.writelines(f'Количество элементов: {len(input_text.split())}\n')
        # Записываем строку с суммой элементов
        f.writelines(f'Сумма элементов: {sum(map(int, input_text.split()))}\n')

        n = int(input('Введите индекс элемента (1 <= n <= 9): '))
        # Записываем строку с элементами до n-1, умноженнными на элемент n
        f.writelines(
            f'Элементы до n-1 умножены на элемент n: {" ".join([str(int(i) * n) for i in input_text.split()[:n]])}')
