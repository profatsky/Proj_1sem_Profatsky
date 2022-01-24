# Вариант 19
# Получить интерфейс максимально приближенный к https://www.bestfree.ru/uslugi/constructors/SozdanieSaytaNaUcoz_3.png

from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.title("ПЗ 12 2")
root.geometry("960x650")
root.resizable(width=False, height=False)


# Функция-обработчик события "закрытие главного окна"
def close():
    root.destroy()
    root.quit()


# Создаю холст, на котором впоследствии буду размещать фигуры и объекты
canvas = Canvas(root, width=960, height=650, bg="white")
canvas.place(x=0, y=0)

canvas.create_rectangle(30, 66, 930, 114, fill="#00AEEF", outline="#00AEEF")  # синий прямоугольник
canvas.create_polygon([461, 114], [500, 114], [480, 127], fill="#00AEEF", outline="#00AEEF")  # синий треугольник

canvas.create_line(30, 115, 30, 650, fill="#E3E3E3")  # линия слева
canvas.create_line(930, 115, 930, 650, fill="#E3E3E3")  # линия справа

# Пунктирные линии
canvas.create_line(30, 220, 930, 220, fill="#E3E3E3", dash=1)
canvas.create_line(30, 350, 930, 350, fill="#E3E3E3", dash=1)
canvas.create_line(30, 477, 930, 477, fill="#E3E3E3", dash=1)

# Заголовок "Регистрация"
header_lbl_1 = Label(root, text="Регистрация", font=("Arial", 22),  bg="white", fg="#00AEEF")
header_lbl_1.place(x=42, y=10)

# Заголовок по центру "Создание нового сайта"
header_lbl_2 = Label(root, text="Создание нового сайта", font=("Arial", 18), bg="#00AEEF", fg="white")
header_lbl_2.place(x=352, y=75)

# Поля для ввода информации
# Email
email_lbl = Label(root, text="Email", font=("Arial", 10, "bold"), bg="white", fg="#0A82D1")
email_lbl.place(x=290, y=142)
email_ent = Entry(root, bg="white", width=24, font=("Arial", 16))
email_ent.place(x=337, y=140)

# Пароль
password_lbl = Label(root, text="Пароль", font=("Arial", 10, "bold"), bg="white", fg="#0A82D1")
password_lbl.place(x=277, y=183)
password_ent = Entry(root, bg="white", width=24, font=("Arial", 16))
password_ent.place(x=337, y=180)

# Имя
first_name_lbl = Label(root, text="Имя", font=("Arial", 10, "bold"), bg="white", fg="#0A82D1")
first_name_lbl.place(x=300, y=232)
first_name_ent = Entry(root, bg="white", width=24, font=("Arial", 16))
first_name_ent.place(x=337, y=230)

# Фамилия
last_name_lbl = Label(root, text="Фамилия", font=("Arial", 10, "bold"), bg="white", fg="#0A82D1")
last_name_lbl.place(x=265, y=273)
last_name_ent = Entry(root, bg="white", width=24, font=("Arial", 16))
last_name_ent.place(x=337, y=270)

# Никнейм
nickname_lbl = Label(root, text="Никнейм", font=("Arial", 10, "bold"), bg="white", fg="#0A82D1")
nickname_lbl.place(x=269, y=314)
nickname_ent = Entry(root, bg="white", width=24, font=("Arial", 16), )
nickname_ent.place(x=337, y=311)

# Дата рождения
date_lbl = Label(root, text="Дата рождения", font=("Arial", 10, "bold"), bg="white", fg="#0A82D1")
date_lbl.place(x=225, y=363)

# Выпадающий список с днями
day = Combobox(root, values=[i for i in range(1, 32)], width=3, font=("Arial", 14))
day.place(x=337, y=361)

# Выпадающий списоок с месяцами
month = Combobox(
    root,
    values=["January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"],
    width=10, font=("Arial", 14)
)
month.place(x=405, y=361)

# Выпадающий список с годами
year = Combobox(
    root,
    values=[i for i in range(1950, 2022)],
    width=5, font=("Arial", 14)
)
year.place(x=550, y=361)

# Радиокнопка для выбора пола
pol_lbl = Label(root, text="Пол", font=("Arial", 10, "bold"), bg="white", fg="#0A82D1")
pol_lbl.place(x=301, y=402)

var = IntVar()
male_rbtn = Radiobutton(root, text="Мужчина", font=("Arial", 10), variable=var, value=1, bg="white")  # мужской пол
male_rbtn.place(x=337, y=400)
female_rbtn = Radiobutton(root, text="Женщина", font=("Arial", 10), variable=var, value=2, bg="white")  # женский пол
female_rbtn.place(x=417, y=400)

# Место проживания
city_lbl = Label(root, text="Место проживания", font=("Arial", 10, "bold"), bg="white", fg="#0A82D1")
city_lbl.place(x=200, y=441)

# Выпадающий список с городами
city_combobox = Combobox(
    root,
    values=["Ростов-на-Дону", "Москва", "Санкт-Петербург", "Другой город"],
    width=23,
    font=("Arial", 16)
)
city_combobox.place(x=337, y=439)

# Код безопасности
code_ent = Entry(root, bg="white", width=6, font=("Arial", 16))
code_ent.place(x=337, y=488)

code_lbl = Label(root, text="Код безопасности", font=("Arial", 10, "bold"), bg="white", fg="#0A82D1")
code_lbl.place(x=207, y=491)

# Подтверждение условий пользователя
access_cbtn = Checkbutton(root, text="Подтверждаю", font=("Arial", 10), bg="white")
access_cbtn.place(x=333, y=533)

access_lbl_1 = Label(root, text="условия использования", font=("Arial", 10, "underline"), bg="white", fg="#0078CA")
access_lbl_1.place(x=444, y=535)

access_lbl_2 = Label(root, text="uID", font=("Arial", 10, "bold"), bg="white")
access_lbl_2.place(x=593, y=535)

access_lbl_3 = Label(root, text="сообщества", font=("Arial", 10), bg="white")
access_lbl_3.place(x=619, y=535)

access_lbl_4 = Label(
    root,
    text="Мы гарантируем, Ваши конфиденциальные данные никогда не попадут в чужие руки",
    font=("Arial", 7),
    bg="white",
    fg="#C1C1C1"
)
access_lbl_4.place(x=337, y=555)

# Кнопка "регистрация"
register_btn = Button(
    root,
    text="Регистрация",
    font=("Arial", 10, "bold"),
    width=12, bg="#0A82D1",
    fg="white",
    relief=GROOVE
)
register_btn.place(x=337, y=592)

root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()
