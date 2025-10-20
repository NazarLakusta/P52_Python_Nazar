text1 = "Hello"
text2 = 'Python'
text3 = """
Це
        багаторядковий
                        рядок
                                ура!    
"""
print(text3)

# конкатинація , обєднання
greeting = "Hello" + "ItStep!"
print(greeting)

# множення на число
# "xa" + "xa" + "xa" + "xa"....
laugh_1 = "xa"*10
laugh_2 = "xa" + "xa" + "xa" + "xa" + "xa" + "xa" + "xa" + "xa" + "xa" + "xa"
print(laugh_1)
print(laugh_2)


print()

# len - length   , len(zminna)
text4 = "Nazar"
print(f"Довжина {text4}: {len(text4)}")

text5 = "fdasfscvjksdhfjkljfsdhfjkdasncvjksdfhsdjkfhsdjkfhsdjkfhaskdljfhklsda"
print(len(text5))

text6 = "Hello Che!"
print(len(text6))


#зменшення всіх букв
print(text6.lower())

print(text6.upper())

# так, ТАК, тАк, ТаК, таК, тАК, ТАк,

# choice = input("Введи так, щоб продовжити та отримати 1 000 000$: ")
# # ТАк - ТАК
# if choice.lower() == "так":
#     print("Ти виграв 1 000 000$")
# else:
#     print("Навчись писати, ти програв")

# title - перша буква слова з великої
text7 = "nazar fdsfsd"
print(text7.title())

# capitalize - перша буква велика всі решта малі
text7 = "nazar fdsfsd"
print(text7.capitalize())

# swapcase - міняє малі на великі і навпаки
text7 = "naZar fDsfSd"
print(text7.swapcase())





# забирає лишні по краям пробіли
text8 = "           Python its cool         "
print(text8)
print(text8.strip())

# replace - заміна символів
text9 = "banana crazy banana its beatiful , monkey loves banana"
text9_replace = text9.replace("ban","orange")
print(text9_replace)

text9_without_space = text9.replace(" ","")
print(text9_without_space)

# split - розділити по символу
text10 = "ItStep Kiev"
text10_split = text10.split(" ")
print(text10_split)


# перевірка на наявність символ в рядку
text11 = "Python"

print("s" in text11)
print("s" not in text11)
print()

# перевірка на цифру, букви, лише букви і цифри
text12_dig = "01234"
print(text12_dig.isdigit())

text12_alph = "asasdfsad"
print(text12_alph.isalpha())


text12_isalnum = "string123"
print(text12_isalnum.isalnum())