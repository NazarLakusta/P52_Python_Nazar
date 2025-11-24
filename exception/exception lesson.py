# ZeroDivisionError - / 0
# ValueError - невірні дані ( текст замість числа)
# TypeError - операція між несумісними типами (чисто + текст)
# NameError - неоголошенна змінна

# IndexError - індекс виходить за меші

# ZeroDivisonError
try:
    # небезпечний код
    b = 0
    x = 5 / b
    print("Цей рядок не виконається")

except ZeroDivisionError:
    print("Не можна ділии на 0")

# 2 - ValueError
try:
    age = int(input("Введи свій вік: "))
    print(f"Тобі {age} років")

except ValueError:
    print("Треба вводити тільки число!")

# Exception
try:
    num = int(input("Введи число: "))
    print(10/0)
except Exception as e:
    print("Сталася помика",e)




try:
    num = int(input("Введи число: "))
    print(10 / 0)
except (ValueError, ZeroDivisionError):
    print("Ну дивись, або на 0 ділиш або це не число")



print("2 excpet")
# 2 except
try:
    num = int(input("Введи число: "))
    print(10 / 0)

except (ValueError):
    print("це не число")

except (ZeroDivisionError):
    print("ти на 0 ділиш, це як")





