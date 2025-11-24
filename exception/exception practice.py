try:
    num = int(input("Input num: "))

except ValueError:
    print("Це не число")

try:
    a = int(input("Num1: "))
    b = int(input("Num2: "))
    result = a/b

    print(result)


except ValueError:
    print("Це не число")

except ZeroDivisionError:
    print("Ділення на 0 ")


color = ["red","green","blue"]

try:
    index = int(input("Введи індекс (0-2): "))
    print("Вибрнай колір",color[index])

except ValueError:
    print("Це не число")

except IndexError:
    print("Такого індекса немає у списку")



try:
    filename = input("Введіть назву файлу: ")
    file = open(filename,"r",encoding='utf-8')
    print("Вміст файлу: ")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Файл не знайденоо")

