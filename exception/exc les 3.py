class PasswordTooShortError(Exception):
    pass

class InvalidAgeError(Exception):
    pass


try:
    age = int(input("Введи свій вік: "))

    if age < 0:
        raise InvalidAgeError("Вік не може бути відємним")

    if age > 120:
        raise InvalidAgeError("Та не може людині бути за 120")

except InvalidAgeError as e:
    print("Помилка",e)

except ValueError:
    print("Вік має бути числом")

else:
    print("Вік прийнято",age)





try:
    password = input("Введи пароль: ")




    if len(password) < 6:
        raise PasswordTooShortError("Пароль має бути не менше 6")

except PasswordTooShortError as e:
    print("Помилка паролю",e)

else:
    print("Пароль прийнято!")





