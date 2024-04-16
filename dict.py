import tkinter as tk
import sqlite3

class LanguageCardApp():
    global current_id
    current_id = 0
    def ConnectToDatabase():
        try:
            db = sqlite3.connect("dict.db")
            c = db.cursor()
            c.execute(
                "select * from words"
            )
            return db
        except Exception as e:
            print(e)
    def ReadDatabase():
        db = sqlite3.connect("dict.db")
        c = db.cursor()
        c.execute("SELECT foreign_word, russian_word FROM words")
        records = c.fetchall()
        return records



    # Функция для получения следующей пары слов
    def get_next_word():
        db = sqlite3.connect("dict.db")
        c = db.cursor()
        c.execute('SELECT russian, english FROM words WHERE id > ?', (current_id,))
        result = c.fetchone()
        return result

    # Функция для получения предыдущей пары слов
    def get_previous_word():
        db = sqlite3.connect("dict.db")
        c = db.cursor()
        c.execute('SELECT russian, english FROM words WHERE id < ?', (current_id,))
        result = c.fetchone()
        #print(result)
        return result

    def show_next_word():
        current_id += 1
        word = get_next_word()
        if word:
            russian_label.config(text=f"Русский: {word[0]}")
            english_label.config(text=f"Английский: {word[1]}")
        else:
            current_id -= 1

    def show_previous_word():

        if current_id > 1:
            current_id -= 1
            word = get_previous_word()
            russian_label.config(text=f"Русский: {word[0]}")
            english_label.config(text=f"Английский: {word[1]}")

    root = tk.Tk()
    root.title("Карточки")
    root.geometry("500x200")
    global label_text
    label_text = tk.StringVar()
    def replace_word():
        try:
            current_text = label_text.get()
            if current_text == words[0][0]:
                new_text = current_text.replace(words[0][0], words[0][1])
                label_text.set(new_text)
            elif current_text == words[0][1]:
                new_text = current_text.replace(words[0][1], words[0][0])
                label_text.set(new_text)
        except IndexError:
            pass

    def update_label():
        label_text.set(str(words[0][0]))

    global words

    words = ReadDatabase()
    print(words[0][0])
    label_text.set(str(words[0][0]))
    change_word = tk.Button(root, text="Повернуть карточку", command=replace_word)
    #next_word = tk.Button(root, text="Следующая карточка", command=reverse)
    next_button = tk.Button(root, text="Вперед", command=show_next_word)
    next_button.pack(side="left")

    previous_button = tk.Button(root, text="Назад", command=show_previous_word)
    previous_button.pack(side="right")
    label = tk.Label(root, textvariable=label_text, font=("Arial Bold", 20))
    label.pack(pady=40)
    change_word.pack(pady=10)
    #next_word.pack()
    root.mainloop()
