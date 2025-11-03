# Online Python - IDE, Editor, Compiler, Interpreter


# створення функції - def назва_функції():
def hello():
    # тіло функції
    # дії, яякі виконує функція
    print("Привіт Юзер, як справи?")


# виклик функції
hello()


# функції з параметрами - def назва_функції(parametr):
def hello_user(name="Дмитро"):
    print(f"Привіт, {name}! Радий тебе бачити")


# виклик функції з параметром
hello_user("Вася")
hello_user("Назар")
hello_user("Петро")

name_1 = "Степан"
hello_user(name_1)

hello_user()


# функції з двома параметрами
def suma(a, b):
    res = a + b
    print(f"{a} + {b} = {res} ")


suma(2, 5)
suma(1000, 324432)
suma(-45234, 54634)
suma(0, 0)


# практика
def average(a, b, c):
    res = (a + b + c) / 3
    print(f"Середнє {a} {b} {c} = {res}")


average(5, 10, 15)
average(321, 12321, 12321)
average(1, 2, 3)


def time_hello(hour):
    if hour >= 0 and hour <= 6:
        print("Добрної ночі")

    elif hour > 6 and hour <= 12:
        print("Доброго ранку")

    elif hour > 12 and hour <= 17:
        print("Доброго дня")

    elif hour > 17 and hour <= 23:
        print("Доброго вечора")

    else:
        print("Не правильний час")


time_hello(5)
time_hello(10)







