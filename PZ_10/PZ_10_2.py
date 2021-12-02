# Из предложенного текстового файла (text18-19.txt) вывести на экран его содержимое, количество символов , принадлежащих
# к группе букв. Сформировать новый файл, в который поместить текст в стихотворной форме предварительно заменив символы
# верхнего регистра на нижний.

with open('text18-19.txt', 'r', encoding='UTF-8') as inp:
    input_text = inp.read()
    letters = input_text
    symbols = ['.', ',', '!', '?', ' ', '-', '—', '\n']
    for i in symbols:
        letters = letters.replace(" ".join(i), "")

print(f'Содерижимое текстового файла:\n{input_text}\n\nКоличество букв:\n{len(letters)}')

with open('output_task_2.txt', 'w') as out:
    out.writelines(f'{input_text.lower()}')

