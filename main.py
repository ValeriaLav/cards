import tkinter as tk
import sqlite3
from tkinter.messagebox import showwarning
from random import randint
#pyinstaller --onefile --add-data "dict.db;." main.py

class MainWindow:

    def __init__(self, master):
        self.master = master
        self.currentindex = 1
        self.amount_str = self.get_amount_str()
        self.couple_words = self.get_words()
        self.mode = 0 # 0 - по порядку, 1- перемешано



    def CreateInsertWindow(self):

        self.ins_window = tk.Toplevel(self.master)
        self.ins_window.title('Добавить слова')
        self.ins_window.geometry("600x200")
        self.ins_window.resizable(width=False, height=False)

        self.label_russn = tk.Label(self.ins_window, text='Слово на русском*', font=('Arial', 10))
        self.label_russn.place(relx=0.15, rely=0.2, anchor=tk.W)

        self.label_forgn = tk.Label(self.ins_window, text='Слово на иностранном*', font=('Arial', 10))
        self.label_forgn.place(relx=0.65, rely=0.2, anchor=tk.W)

        self.label_group  = tk.Label(self.ins_window, text='Группа слова', font=('Arial', 10))
        self.label_group.place(relx=0.18, rely=0.5, anchor=tk.W)

        self.label_level = tk.Label(self.ins_window, text='Уровень слова', font=('Arial', 10))
        self.label_level.place(relx=0.68, rely=0.5, anchor=tk.W)

        self.entr_russian_word = tk.Entry(self.ins_window, width=40)
        self.entr_russian_word.place(relx=0.05, rely=0.3, anchor=tk.W)

        self.entr_foreign_word = tk.Entry(self.ins_window, width=40)
        self.entr_foreign_word.place(relx=0.55, rely=0.3, anchor=tk.W)

        self.entr_group_word = tk.Entry(self.ins_window, width=40)
        self.entr_group_word.place(relx=0.05, rely=0.6, anchor=tk.W)

        self.entr_level_word= tk.Entry(self.ins_window, width=40)
        self.entr_level_word.place(relx=0.55, rely=0.6, anchor=tk.W)

        self.btn_save = tk.Button(self.ins_window, text="Сохранить", command=self.insert_words)
        self.btn_save.place(relx=0.5, rely=0.9, anchor=tk.S)


    def CreateMainWindow(self):

        self.text_label = tk.Label(self.master, text=self.couple_words[0], font=('Arial', 20))
        self.text_label.pack(side=tk.TOP)

        self.bnt_next = tk.Button(self.master, text="Вперед", command=self.next_word)
        self.bnt_next.place(relx=0.9, rely=0.5, anchor=tk.E)

        self.btn_change = tk.Button(self.master, text="Перевернуть", command=self.replace_word)
        self.btn_change.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.btn_previous = tk.Button(self.master, text="Назад", command=self.prev_word)
        self.btn_previous.place(relx=0.1, rely=0.5, anchor=tk.W)

        self.btn_insert = tk.Button(self.master, text="Добавить слова", command=self.CreateInsertWindow)
        self.btn_insert.place(relx=0.8, rely=0.1)

        self.btn_mix = tk.Button(self.master, text="Перемешать слова", command=self.mix_words)
        self.btn_mix.place(relx=0.05, rely=0.1, anchor=tk.W)

        self.btn_mix = tk.Button(self.master, text="Упорядочить слова", command=self.regularize_words)
        self.btn_mix.place(relx=0.05, rely=0.25, anchor=tk.W)

    def mix_words(self):
        self.mode = 1

    def regularize_words(self):
        self.mode = 0


    def prev_word(self):
        self.curr_couple = self.get_words()
        self.currentindex -= 1
        self.couple_words = self.get_words()
        self.curr_text = self.text_label.cget("text")
        self.text_label.config(text=self.couple_words[1] if self.curr_text == self.curr_couple[1] else self.couple_words[0])

    def replace_word(self):
        self.curr_text = self.text_label.cget("text")
        self.text_label.config(text=self.couple_words[1] if self.curr_text == self.couple_words[0] else self.couple_words[0])

    def next_word(self):
        self.curr_couple = self.get_words()
        if self.mode == 1:
            self.currentindex = randint(0, self.amount_str)
        else:
            self.currentindex += 1
        self.couple_words = self.get_words()
        self.curr_text = self.text_label.cget("text")
        self.text_label.config(text=self.couple_words[1] if self.curr_text == self.curr_couple[1] else self.couple_words[0])

    def get_words(self):
        if self.currentindex <= 0:
            self.currentindex = 1
        conn = sqlite3.connect("dict.db")
        cursor = conn.cursor()
        try:
            # get_count = """ SELECT COUNT(*) FROM WORDS"""
            # cursor.execute(get_count)
            # self.amount_str = cursor.fetchone()
            if self.currentindex > self.amount_str:
                self.currentindex = self.amount_str
            query = f"""SELECT foreign_word , russian_word FROM WORDS where ID = {self.currentindex}"""
            cursor.execute(query)
            c_words = cursor.fetchone()
        except Exception as e:
            print("Ошибка ", e)
        cursor.close()
        conn.close()
        return c_words

    def insert_words(self):
        self.rusn_word = self.entr_russian_word.get()
        self.forgn_word = self.entr_foreign_word.get()
        self.group_word = self.entr_group_word .get()
        self.level_word = self.entr_level_word.get()
        if self.rusn_word == "" or self.forgn_word == "":
            tk.messagebox.showwarning(title="Предупреждение", message="пустые строки не допустимы")
            return
        elif any(ch.isdigit() for ch in self.rusn_word) or any(ch.isdigit() for ch in self.forgn_word):
            tk.messagebox.showwarning(title="Предупреждение", message="недопустимые символы")

        insert_words = f""" INSERT INTO words (foreign_word, russian_word, level_word, group_word) 
            VALUES ( '{self.forgn_word}' ,  '{self.rusn_word}', '{self.level_word}', '{self.group_word}') """

        if self.group_word == "":
            insert_words = f""" INSERT INTO words (foreign_word, russian_word, level_word, group_word) 
                VALUES ( '{self.forgn_word}' ,  '{self.rusn_word}', '{self.level_word}', NULL) """
        if self.level_word == "":
            insert_words = f""" INSERT INTO words (foreign_word, russian_word, level_word, group_word) 
                VALUES ( '{self.forgn_word}' ,  '{self.rusn_word}', NULL, '{self.group_word}') """

        conn = sqlite3.connect("dict.db")
        cursor = conn.cursor()
        try:
            print(insert_words)
            cursor.execute(insert_words)
        except Exception as e:
            print("Ошибка ", e)
        conn.commit()
        cursor.close()
        conn.close()
    def get_amount_str(self):
        conn = sqlite3.connect("dict.db")
        cursor = conn.cursor()
        try:
            get_count = """ SELECT COUNT(*) FROM WORDS"""
            cursor.execute(get_count)
            amount_str = cursor.fetchone()
        except Exception as e:
            print("Ошибка ", e)
        cursor.close()
        conn.close()
        return amount_str[0]




def main():
    root = tk.Tk()
    root.geometry("510x260")
    root.title("Карточки")
    root.resizable(width=False, height=False)
    app = MainWindow(root)
    app.CreateMainWindow()
    root.mainloop()


if __name__ == "__main__":
    main()