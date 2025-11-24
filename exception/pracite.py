class WeakPasswordError(Exception):
    pass

try:
    password = input("Введіть пароль: ")

    if len(password) < 6:
        raise WeakPasswordError("Пароль занадто короткий!")
    if password.isdigit():
        raise WeakPasswordError("Пароль не може складатися лише з цифр!")
    if password.isalpha():
        raise WeakPasswordError("Пароль має містити хоча б одну цифру!")

except WeakPasswordError as e:
    print("❌", e)
else:
    print("✔️ Пароль прийнято!")


class InvalidEmailError(Exception):
    pass

try:
    email = input("Введіть email: ")

    if "@" not in email:
        raise InvalidEmailError("Email має містити '@'")
    if "." not in email[email.index("@"):]:
        raise InvalidEmailError("Email має містити '.' після '@'")
    if email[0].isdigit():
        raise InvalidEmailError("Email не може починатися з цифри")

except InvalidEmailError as e:
    print("❌", e)
else:
    print("✔️ Email правильний:", email)


class TooSmallPaymentError(Exception):
    pass

try:
    amount = float(input("Введіть суму оплати: "))
    if amount < 50:
        raise TooSmallPaymentError("Мінімальна оплата — 50 грн!")
except ValueError:
    print("❌ Введіть число!")
except TooSmallPaymentError as e:
    print("❌", e)
else:
    print("✔️ Оплату прийнято:", amount, "грн")


products = ["Milk", "Bread", "Apple"]

try:
    title = input("Введіть назву товару: ")
    if title not in products:
        raise ValueError("Такого товару немає!")
except ValueError as e:
    print("❌", e)
else:
    print("✔️ Продукт знайдено:", title)



class InvalidLoginError(Exception):
    pass

try:
    login = input("Введіть логін: ")

    if len(login) < 4:
        raise InvalidLoginError("Логін має бути не менше 4 символів!")
    if " " in login:
        raise InvalidLoginError("Логін не може містити пробіли!")
    if login[0].isdigit():
        raise InvalidLoginError("Логін не може починатися з цифри!")

except InvalidLoginError as e:
    print("❌", e)
else:
    print("✔️ Логін прийнято!")


class SpeedLimitError(Exception):
    pass

try:
    speed = int(input("Введіть швидкість авто: "))

    if speed < 0:
        raise SpeedLimitError("Швидкість не може бути негативною!")
    if speed > 200:
        raise SpeedLimitError("Нереальна швидкість! 🚀")
    if speed > 90:
        raise SpeedLimitError("Перевищення швидкості! ⚠️")

except ValueError:
    print("❌ Введіть число!")
except SpeedLimitError as e:
    print("❌", e)
else:
    print("✔️ Швидкість допустима:", speed)


class InvalidOperatorError(Exception):
    pass

class TooLargeResultError(Exception):
    pass

try:
    a = float(input("Введіть перше число: "))
    op = input("Введіть оператор (+, -, *): ")
    b = float(input("Введіть друге число: "))

    if op not in ["+", "-", "*"]:
        raise InvalidOperatorError("Невідомий оператор!")

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b

    if result > 10000:
        raise TooLargeResultError("Результат занадто великий!")

    print("Результат:", result)

except ValueError:
    print("❌ Введіть числа!")
except InvalidOperatorError as e:
    print("❌", e)
except TooLargeResultError as e:
    print("❌", e)
