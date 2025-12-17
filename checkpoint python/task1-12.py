price = float(input("Ввів ціну: "))
paid = float(input("Введіть оплату: "))

change = paid - price
change = round(change,2)

print(f"Ваша здача: {change} грн.")


c = float(input("Температура в С: "))
f = c*9/5+32
print(f"Фарангейти: {f}")


km = float(input("Кілометри: "))

if km<=2:
    price=60

else:
    price = 60 + (km-2) * 15

print(f"Вартість: {price}")



# R/P/S
from random import *

while True:
    p1 = input("Гравець1: К/Н/П: ").lower()
    bot = choice(["к","н","п"])

    if p1 == bot:
        print("Нічия")

    elif p1 == "к" and bot == "н":
        print("P1 won")

    elif p1 == "п" and bot == "к":
        print("P1 won")

    elif p1 == "н" and bot == "п":
        print("P1 won")

    else:
        print("Bot won")

    choice_y_n = input("Бажаєш зіграти ще раз? т/н: ").lower()
    if choice_y_n == "н":
        break



n = int(input("Кількість чисел: "))
numbers = []

for _ in range(n):
    numbers.append(float(input()))

total = sum(numbers)
print(f"total: {total}")



items = []
num = [12,32,12,3,12]

while True:
    text = input()
    if text == "stop":
        break
    items.append(text)

longest = max(items, key=len)
print(f"Найдовший: {longest} ")
print(f"Кількість: {len(items)}")


def is_even(n):
    return n % 2 == 0

def sum_list(nums):
    total = 0
    for n in nums:
        total+=n

    return total

nums = [23,32,34,2342,32,32]
print(f"Сума: {sum_list(nums)}")





class Student:
    def __int__(self,name):
        self.name = name
        self.grades = []

    def add_grade(self,g):
        self.grades.append(g)


    def average(self):
        if not self.grades:
            return 0

        return sum(self.grades)/len(self.grades)

    def info(self):
        print(self.name,"Середнів бал:",self.average())


nazar = Student("Nazar")

nazar.add_grade(10)
nazar.add_grade(11)
nazar.add_grade(9)

nazar.info()







