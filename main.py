import tkinter as tk
import sqlite3


class LanguageCards:

    def __init__(self, master):
        self.master = master
        self.currentindex = 1
        self.couple_words = self.get_words()

    def CreateWindow(self):

        self.text_label = tk.Label(self.master, text=self.couple_words[0], font=('Arial', 20))
        self.text_label.pack(side=tk.TOP)

        self.bnt_next = tk.Button(self.master, text="Вперед", command=self.next_word)
        self.bnt_next.place(relx=0.9, rely=0.5, anchor=tk.E)

        self.btn_change = tk.Button(self.master, text="Перевернуть", command=self.replace_word)
        self.btn_change.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.btn_previous = tk.Button(self.master, text="Назад", command=self.prev_word)
        self.btn_previous.place(relx=0.1, rely=0.5, anchor=tk.W)

    def prev_word(self):
        self.currentindex -= 1
        self.couple_words = self.get_words()
        print(self.couple_words)
        self.text_label.config(text=self.couple_words[0])

    def replace_word(self):
        self.curr_text = self.text_label.cget("text")
        self.text_label.config(text=self.couple_words[1] if self.curr_text == self.couple_words[0] else self.couple_words[0])

    def next_word(self):
        self.currentindex += 1
        self.couple_words = self.get_words()
        print(self.couple_words)
        self.text_label.config(text=self.couple_words[0])

    def get_words(self):
        #индекс уходит слишком далеко !!!!!!!!!
        if self.currentindex <= 0:
            return self.couple_words
        conn = sqlite3.connect("dict.db")
        cursor = conn.cursor()
        try:
            query = f"""select foreign_word , russian_word from words where ID = {self.currentindex}"""
            cursor.execute(query)
            couple_words = cursor.fetchone()
            #print(type(couple_words))
        except Exception as e:
            print("Ошибка ", e)
        cursor.close()
        conn.close()
        return couple_words


def main():
    root = tk.Tk()
    root.geometry("500x250")
    root.title("Карточки")
    app = LanguageCards(root)
    app.CreateWindow()

    root.mainloop()

if __name__ == "__main__":

    main()