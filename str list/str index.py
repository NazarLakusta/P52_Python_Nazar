word = "Ukraine"

small_str_0 = word[6] + word[0]

print(small_str_0)


text = "Programming fdsfds fdsfds dfsdf sdfsd dsfsd"
print(len(text))
# вказувати з якого по який індекс іде текст [0:6]
print(text[0:6])

print(text[6:-1])
print(text[6:len(text)])
print(text[6:])

print(text[:10])

# вказувати крок через який буде братись символ [::1]
print(text[::2])

text_1 = "Nazar"
print(text_1[::-1])


text_reverse = input("Напиши слово на перевірку дзеркальності: ")

if text_reverse == text_reverse[::-1]:
    print("Дзеркальне")

else:
    print("Не дзеркальне")

# підрахунок кількості сиволу
print(f"Кількість символу а: {text_reverse.count("a")}")

