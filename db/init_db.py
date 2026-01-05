# 1) connect - підключення
# 2) cursor - канал запити
# 3) execute - виконати SQL
# 4) fetch*() - забрати результат з каналу
# 5) commit() - зберегти зміни
# 6) close() - закрити

import sqlite3

# створення/підключення бази даних
conn = sqlite3.connect("school.db")

# створення курсора
cursor = conn.cursor()

# виконуємо запит
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
group_name TEXT
)
""")


conn.commit()
conn.close()





