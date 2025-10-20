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

choice = input("Введи так, щоб продовжити та отримати 1 000 000$: ")
# ТАк - ТАК
if choice.lower() == "так":
    print("Ти виграв 1 000 000$")
else:
    print("Навчись писати, ти програв")

# title - перша буква слова з великої
text7 = "nazar fdsfsd"
print(text7.title())

# capitalize - перша буква велика всі решта малі
text7 = "nazar fdsfsd"
print(text7.capitalize())
