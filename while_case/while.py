
i = 0


while i<5:
    print(f"i = {i}")
    i += 1
print(f"i after while = {i}")


while True:
    print(f"i = {i}")
    i += 1
    if i > 1000:
        choice = input("Мені продовжувати рахувати? Т/Н - ")
        if choice == "Так" or choice == "Т":
            continue
        else:
            print("Дякую за увагу")
            break




