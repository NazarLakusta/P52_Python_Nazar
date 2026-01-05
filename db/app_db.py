import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()



# добавити інфу про студента у таблицю студенти
# cursor.execute("""
# INSERT INTO students (name,age,group_name)
# VALUES (?, ?, ?);
# """, ("Petro",22,"P52"))

# видалити інформацію або по умові, або всіх
# cursor.execute("DELETE FROM students WHERE id = ?;",(3,))
# cursor.execute("DELETE FROM students;")


# # оновити інформацію
# cursor.execute("""UPDATE students
#                SET age = ?
#                WHERE name = ?;
#                """,(20,"Vasia"))


cursor.execute("""
SELECT * FROM students;
""")

print("====ALL=====")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("====NAME-AGE=====")
cursor.execute("""
SELECT name, age 
FROM students;
""")

rows = cursor.fetchall()
for row in rows:
    print(row)


print("====P52=====")
cursor.execute("""
SELECT * 
FROM students
WHERE group_name = ?;
""",("P52",)
    )

rows = cursor.fetchall()
for row in rows:
    print(row)


print("====SORT BY AGE=====")
cursor.execute("""
SELECT name, age, group_name 
FROM students
WHERE age IS NOT NULL
ORDER BY group_name DESC;
""")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()