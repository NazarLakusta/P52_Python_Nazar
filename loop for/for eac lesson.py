students = ["Nazar","Olha","Ihor","Sophia"]


for student in students:

    if len(student) < 5:
        print(student)


print(students)



grades = [10,11,6,12,7,2,3,10,12,11,5,7]

excellent = 0
needs_help = 0

for grade in grades:
    if grade >= 10:
        excellent += 1

    elif grade < 10:
        needs_help += 1


print("Відмінники: ",excellent)
print("Допомогти: ",needs_help)




files = ["photo1.jpg","music.mp3","photo2.jpg","text.txt","file.png"]


for file in files:
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith("webp"):
        print("Зображення: ",file)


currencies = ["USD","EUR","UAH"]

for currency in currencies:
    if currency == "USD":
        print("Долар США")

    elif currency == "UAH":
        print("Гривні")

    elif currency == "EUR":
        print("Євро")
