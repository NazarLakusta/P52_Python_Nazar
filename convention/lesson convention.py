# спочатку імпорт потім уже фром
import os
import sys

from random import randint



if(x==5):
    print("Hello")

# між операторами - пробіли
a = 5
b = 10
c = 15
sum = a + (b + c)

# текс через ентер розділяєте
text = ("gfdgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
        "gggggggggggggggggggggggggggg")

# між функціями 2 пустих рядка
def greet(name):
    print(f"Привіт,{name}")


def add(a,b):
    return a + b


# snake case
my_var_1 = 10

def get_random_number():
    pass


speed = input("Input your speed: ")

if speed > 90:
    print("Перевищення")


# використовуємо константи, пишемо капсом
MAX_SPEED = 90

if speed > MAX_SPEED:
    print("Перевищення")



# докстрінги та коментарі
def greet(name):
    """Виводить привітання для користувача"""
    print(f"Привіт,{name}!")


#Якщо користувач написав No, вийти з циклу
if choice == "No":
    break

# Можете вказувати який тип даних хочете опрацьовувати
def add(a : int, b : int) -> int:
    return a + b


add(5.4,6.2)