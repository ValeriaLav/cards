import sqlite3


con = sqlite3.connect("dict.db")

cursor = con.cursor()

try:
    cursor.execute("""CREATE TABLE IF NOT EXISTS words
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                foreign_word VARCHAR(255),
                russian_word VARCHAR(255),
                level_word VARCHAR(255),
                group_word VARCHAR(255) )
            """)

# try :
#     cursor.execute("""drop  TABLE words""")

except Exception as e:
    print(e)

with open('test.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()

for line in lines:
    data = line.strip().split(',')
    cursor.execute('''
        INSERT INTO words (foreign_word, russian_word, level_word, group_word)
        VALUES (?, ?, ?, ?)
    ''', data)


con.commit()

# Закрываем соединение
con.close()