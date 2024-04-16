import tkinter as tk
import sqlite3

class LanguageCardApp:
    def __init__(self, words):
        self.words = words

    def replace_word(self):
        try:
            current_text = self.label_text.get()
            if current_text == self.words[0][0]:
                new_text = current_text.replace(self.words[0][0], self.words[0][1])
                self.label_text.set(new_text)
            elif current_text == self.words[0][1]:
                new_text = current_text.replace(self.words[0][1], self.words[0][0])
                self.label_text.set(new_text)
        except IndexError:
            pass

    def OpenWindow(self):
        root = tk.Tk()
        root.title("Карточки")
        root.geometry("500x200")
        label_text = tk.StringVar()
        print(self.words[0])
        label_text.set(self.words[0][0])
        change_word = tk.Button(root, text="Повернуть карточку", command=self.replace_word)
        #next_word = tk.Button(root, text="Следующая карточка", command=reverse)
        #next_button = tk.Button(root, text="Вперед", command=show_next_word)
        #next_button.pack(side="left")

        #previous_button = tk.Button(root, text="Назад", command=show_previous_word)
        #previous_button.pack(side="right")
        label = tk.Label(root, textvariable=label_text, font=("Arial Bold", 20))
        label.pack(pady=40)
        change_word.pack(pady=10)
        #next_word.pack()
        root.mainloop()
s = LanguageCardApp([['123', '3333']])
s.OpenWindow()