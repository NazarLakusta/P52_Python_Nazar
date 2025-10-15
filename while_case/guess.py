# Введіть якесь число від 1 до 100 - 50
# Загадне число більше
# Введіть якесь число від 1 до 100 - 90
# загадане число менше
# Введіть якесь число від 1 до 100 - 75
# Ви відгадали. Дякую за гру!


from random import *


bot_number = randint(1,100)
num_att = 0
while True:
    print(f"Спроба №{num_att}")
    number = int(input("Введи число: "))
    if number < bot_number:
        print("Загадне більше")

    elif number > bot_number:
        print("Загадне менше")

    else:
        print("WIN")
        break
    
    num_att += 1
    if num_att > 10:
        print("Спроби закінчились")
        print("Дякую за гру")
        break