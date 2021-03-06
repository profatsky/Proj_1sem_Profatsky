# Вариант 19
# Из исходного текстового файла (pazzl.html) выбрать все html-коды изображений. Посчитать их количество.
import re

with open("pazzl.html", "r", encoding="utf-8") as file:  # открываем файл pazzl.html на чтение
    text = file.read()  # считываем содержимое документа
    reg = re.findall(r'src="(.+?)"', text)  # ищем все подстроки, подходящие под шаблон, в тексте
    print(f"HTML-коды изображений: {reg}\nКоличество изображений: {len(reg)}")  # вывод результата
