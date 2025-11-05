
# приклад функція у функції

def calcute_price(price ,count):
    return pric e *count

def print_check(name ,price ,count):
    suma = calcute_price(price ,count)
    print(f"Товар: {name} - {count} шт.")
    print(f"Загальна вартість: {suma} грн.")


print_check("Кава" ,45 ,3)


# ще один приклад

def hello():
    print("Вітаю у програмі")

def main_part():
    hello()
    print("Тут буде головна логіка")


main_part()





def area(side):
    return side *side


square_1 = area(5)

square_2 = area(3)
print(square_1 + square_2)

def print_area():
    print(f"Площа: {square_1}")

print_area()
