import tkinter as tk

file = 'dict.txt'

with open(file, 'r', encoding='utf-8') as f:
    root = tk.Tk()
    root.title("Карточки")
    root.geometry("500x200")
    label_text = tk.StringVar()

    def replace_word():
        try :
            current_text = label_text.get()
            if current_text == words[0]:
                new_text = current_text.replace(words[0], words[1])
                label_text.set(new_text)
            elif current_text == words[1]:
                new_text = current_text.replace(words[1], words[0])
                label_text.set(new_text)
        except IndexError:
            pass

    def update_label():
        label_text.set(str(words[0]))

    def reverse():
        global words
        words = f.readline().strip().replace('–', '-').replace(':', '-')
        words = words.split('-')
        update_label()
        return words
    words = reverse()

    label_text.set(str(words[0]))
    change_word = tk.Button(root, text="Повернуть карточку", command=replace_word)
    next_word = tk.Button(root, text="Следующая карточка", command=reverse)
    label = tk.Label(root, textvariable=label_text, font=("Arial Bold", 20))
    label.pack(pady=40)

    change_word.pack(pady=10)
    next_word.pack()

    root.mainloop()


# мне нужно написать приложение на python. у меня есть пара слов слово1 и слово2 . есть функция функция1 которая меняет пару слов на новую. еще есть функция функция2 которая при нажатии меняет слово1 на слово2 . напиши код с помощью tkinter что бы при нажатии на кнопку2 менялась пара слов и при нажатии на кнопку1 слово1 менялось на слово2 и наоборот

#
# import tkinter as tk
#
#
# class WordChangerApp:
#     with open('dict.txt', 'r', encoding='utf-8') as f:
#         def __init__(self, root):
#             self.root = root
#             self.root.title("Смена слов")
#
#             # Исходные слова
#             self.word1 = "слово1"
#             self.word2 = "слово2"
#
#             # Создаем метку для отображения текущей пары слов
#             self.label_text = tk.Label(root, text=f"{self.word1} - {self.word2}")
#             self.label_text.pack(pady=10)
#             self.words = self.reverse()
#             # Создаем кнопку для смены пары слов
#             self.change_button = tk.Button(root, text="Сменить пару слов", command=self.change_words)
#             self.change_button.pack()
#
#             # Создаем кнопку для обмена словами
#             self.swap_button = tk.Button(root, text="Обменять слова", command=self.swap_words)
#             self.swap_button.pack()
#             self.file = 'dict.txt'
#
#
#
#         def replace_word(self):
#             current_text = self.label_text.get()
#             print(words)
#             if current_text == words[0]:
#                 new_text = current_text.replace(words[0], words[1])
#                 self.label_text.set(new_text)
#             elif current_text == words[1]:
#                 new_text = current_text.replace(words[1], words[0])
#                 self.label_text.set(new_text)
#
#         def update_label(self):
#             self.label_text.set(str(words[0]))
#
#         def reverse(self):
#             global words
#             words = self.f.readline().strip().split('-')
#             print(words)
#             self.update_label()
#             return words
#
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = WordChangerApp(root)
#     root.mainloop()
