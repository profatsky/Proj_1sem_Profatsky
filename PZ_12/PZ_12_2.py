# Вариант 19
# Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ №№ 3 – 8.
# Выбрана задача №3.1

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("ПЗ 12 2")
root.geometry("640x360")
root["bg"] = "#FFF8DC"
root.resizable(width=False, height=False)


# Функция-обработчик события "закрытие главного окна"
def close():
    root.destroy()
    root.quit()


# Функция-обработчик события "нажатие на кнопку"
def process():
    try:
        # Присвоение переменным значений, полученных из полей ввода
        a, b, c = int(first_ent.get()), int(second_ent.get()), int(third_ent.get())
        # Проверка истинности высказывания
        if a == b or a == c or a == b == c or b == c:
            messagebox.showinfo("Истина", "Среди трех данных чисел есть как минимум одна пара совпадающих")
        else:
            messagebox.showinfo("Ложь", "Среди трех данных числе нет ни одной пары совпадающих")
    except ValueError:
        messagebox.showerror("Ошибка", "Некорректный ввод")


# Условие задачи
text = Label(
    root,
    text="Проверить истинность высказывания:\n«Среди трех данных целых чисел есть хотя бы одна пара совпадающих»",
    font=("Arial", 12),
    bg="#FFF8DC"
)
text.pack()

# Первое поле ввода
first_lbl = Label(root, text="Первое число", font=("Arial", 12), bg="#FFF8DC")
first_lbl.place(x=200, y=90)
first_ent = Entry(root, font=("Arial", 12), width=7)
first_ent.place(x=340, y=90)

# Второе поле ввода
second_lbl = Label(root, text="Второе число", font=("Arial", 12), bg="#FFF8DC")
second_lbl.place(x=200, y=140)
second_ent = Entry(root, font=("Arial", 12), width=7)
second_ent.place(x=340, y=140)

# Третье поле ввода
third_lbl = Label(root, text="Третье число", font=("Arial", 12), bg="#FFF8DC")
third_lbl.place(x=200, y=190)
third_ent = Entry(root, font=("Arial", 12), width=7)
third_ent.place(x=340, y=190)

# Кнопка "Проверить"
btn = Button(root, text="Проверить", font=("Arial", 12), bg="blue", fg="white", command=process)
btn.place(x=270, y=250)

root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()
