# Приложение ГРУЗОВЫЕ ПЕРЕВОЗКИ для некоторой организации. БД должна
# содержать таблицу Перевозки со следующей структурой записи: маршрут, фамилия
# водителя, даты отправки и прибытия, масса груза.
# БД должна обеспечивать получение информации по массе груза.

import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#3CA0D0', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="images/add.gif")
        self.btn_open_dialog = tk.Button(
            toolbar, text='Добавить перевозку',
            command=self.open_dialog, bg='#ffffff',
            bd=0,
            compound=tk.TOP,
            image=self.add_img
        )
        self.btn_open_dialog.pack(side=tk.LEFT, padx=2)

        self.update_img = tk.PhotoImage(file="images/update.gif")
        btn_edit_dialog = tk.Button(
            toolbar,
            text="Редактировать",
            command=self.open_update_dialog,
            bg='#ffffff',
            bd=0, compound=tk.TOP,
            image=self.update_img
        )
        btn_edit_dialog.pack(side=tk.LEFT, padx=2)

        self.delete_img = tk.PhotoImage(file="images/delete.gif")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#ffffff',
                               bd=0, compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT, padx=2)

        self.search_img = tk.PhotoImage(file="images/search.gif")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#ffffff',
                               bd=0, compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT, padx=2)

        self.refresh_img = tk.PhotoImage(file="images/refresh.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#ffffff',
                                bd=0, compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT, padx=2)

        self.tree = ttk.Treeview(
            self,
            columns=('transportation_id', 'route', 'shipment', 'arrival', 'driver', 'mass'),
            height=15,
            show='headings'
        )

        self.tree.column('transportation_id', width=50, anchor=tk.CENTER)
        self.tree.column('route', width=180, anchor=tk.CENTER)
        self.tree.column('driver', width=140, anchor=tk.CENTER)
        self.tree.column('shipment', width=140, anchor=tk.CENTER)
        self.tree.column('arrival', width=140, anchor=tk.CENTER)
        self.tree.column('mass', width=140, anchor=tk.CENTER)

        self.tree.heading('transportation_id', text='ID')
        self.tree.heading('route', text='Маршрут')
        self.tree.heading('driver', text='Водитель')
        self.tree.heading('shipment', text='Дата отправки')
        self.tree.heading('arrival', text='Дата прибытия')
        self.tree.heading('mass', text='Масса груза (т.)')

        self.tree.pack()

    def records(self, route, shipment, arrival, driver, mass):
        self.db.insert_data(route=route, shipment=shipment, arrival=arrival, driver=driver, mass=mass)
        self.view_records()

    def update_record(self, route, shipment, arrival, driver, mass):
        self.db.cur.execute(
            """UPDATE transportation SET route = ?, shipment = ?, arrival = ?, driver = ?, mass = ? 
            WHERE transportation_id = ?""",
            (route, shipment, arrival, driver, mass, self.tree.set(self.tree.selection()[0], '#1'))
        )
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM transportation""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute(
                """DELETE FROM transportation WHERE transportation_id = ?""",
                (self.tree.set(selection_item, '#1'),)
            )
        self.db.con.commit()
        self.view_records()
    # def search_records(self, user_id):
        # user_id = ("%" + user_id + "%",)
        # self.db.cur.execute("""SELECT * FROM users WHERE name LIKE ?""", user_id)
        # [self.tree.delete(i) for i in self.tree.get_children()]
        # [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def search_records(self, mass):
        self.db.cur.execute("""SELECT * FROM transportation WHERE mass > ?""", (mass,))
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить перевозки')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Маршрут')
        label_description.place(x=50, y=25)
        self.entry_route = ttk.Entry(self)
        self.entry_route.place(x=170, y=25)

        label_name = tk.Label(self, text='Фамилия водителя')
        label_name.place(x=50, y=50)
        self.entry_driver = ttk.Entry(self)
        self.entry_driver.place(x=170, y=50)

        label_sex = tk.Label(self, text='Дата отправки')
        label_sex.place(x=50, y=75)
        self.entry_shipment = ttk.Entry(self)
        self.entry_shipment.place(x=170, y=75)

        label_old = tk.Label(self, text='Дата прибытия')
        label_old.place(x=50, y=100)
        self.entry_arrival = ttk.Entry(self)
        self.entry_arrival.place(x=170, y=100)

        label_old = tk.Label(self, text='Масса груза')
        label_old.place(x=50, y=125)
        self.entry_mass = ttk.Entry(self)
        self.entry_mass.place(x=170, y=125)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind(
            '<Button-1>', lambda event: self.view.records(
                route=self.entry_route.get(),
                driver=self.entry_driver.get(),
                shipment=self.entry_shipment.get(),
                arrival=self.entry_arrival.get(),
                mass=self.entry_mass.get()
            )
        )

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.view = app

        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=170)
        btn_edit.bind(
            '<Button-1>', lambda event: self.view.update_record(
                route=self.entry_route.get(),
                shipment=self.entry_shipment.get(),
                arrival=self.entry_arrival.get(),
                driver=self.entry_driver.get(),
                mass=self.entry_mass.get()
            )
        )
        self.btn_ok.destroy()


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.view = app

        self.title("Поиск")
        self.geometry("250x200+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск записей по массе")
        label_search.place(x=50, y=20)

        label_hint = tk.Label(self, text="Будут выведены записи,\nгде масса больше указанного числа")
        label_hint.place(x=20, y=120)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=50, y=50, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=135, y=80)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=50, y=80)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add=True)


class DB:
    def __init__(self):
        with sq.connect('transportation.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS transportation (
                transportation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                route TEXT NOT NULL,
                shipment DATE NOT NULL,
                arrival DATE NOT NULL,
                driver TEXT NOT NULL,
                mass INT NOT NULL
                )""")

    def insert_data(self, route, driver, shipment, arrival, mass):
        self.cur.execute(
            """INSERT INTO transportation (route, driver, shipment, arrival, mass) VALUES (?, ?, ?, ?, ?)""",
            (route, driver, shipment, arrival, mass))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Грузовые перевозки")
    root.geometry("800x400+300+200")
    root.iconphoto(True, tk.PhotoImage(file="images/truck.png"))
    root.resizable(False, False)
    root.mainloop()
