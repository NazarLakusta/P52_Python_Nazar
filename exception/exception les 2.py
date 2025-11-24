try:
    num = int(input("Введи число: "))

except ValueError:
    print("Це не число")

else:
    print("Молодець! Ти нарештів ввів число ",num)

finally:
    print("Оерація завершена(успіх чи помилка - неважливо)")