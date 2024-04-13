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

