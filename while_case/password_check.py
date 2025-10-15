password = "1710"

attempt = ""

num_attempts = 1


while True:
    print(f"\nКількість спроб залишилось {13-num_attempts}")
    if num_attempts >= 10:
        print("\nПідказка: Дата народження")
    print(f"\nТвоя спроба №{num_attempts}")
    attempt = input("Введи пароль: ")


    if attempt == password:
        print("Ти увійшов!")
        print(f"З {num_attempts} спроби")
        break
    else:
        print("Невірно, спробуй ще")

    if num_attempts == 12:
        print("\nТи не пройшов перевірку")
        print("Пака")
        num_attempts = 0
        break

    num_attempts += 1
