list_of_student = ["Bogdan","Dima","Nikita","Artem","Maks","Mykola"]
list_of_num = [1421,12312,12312,12312,3232]
list_of_bool = [True,False,True,True]
list_of_all = ["Bohdan",23,True,"1fdsf",False]

print(list_of_student[0])

list_blank = []

# добавити елемент у список
list_blank.append("Chernivtsi")
print(list_blank)

list_blank.append("Kiev")
print(list_blank)

# добавити елемент в конкретне місце
list_blank.insert(1,"Lviv")
print(list_blank)


# добавити декілька
list_blank.extend(["Ivano-Frankivs","Sumy"])
print(list_blank)


# розмір, довжина
print(len(list_blank))


# видалення
# останній
list_blank.pop()
print(list_blank)

# по індексу
list_blank.pop(0)
print(list_blank)

# по значення
list_blank.remove("Kiev")
print(list_blank)

# все очистити
list_blank.clear()
print(list_blank)



list_num = [2,3,53,7,1,5,54,23,64,7]
print(f"К-сть чисел: {len(list_num)}")
print(f"Сума чисел: {sum(list_num)}")
print(f"Максимальне число: {max(list_num)}")
print(f"Мінімальне число: {min(list_num)}")

# сортування
list_num.sort()
print(f"Сортування: {list_num}")

# обернути список
list_num.reverse()
print(f"Реверс: {list_num}")


print(f"Кількість цифри 7 {list_num.count(7)}")
print(f"Індекс цифри 7 {list_num.index(7)}")



list_num_1 = [1,2,3]
list_num_2 = [4,5,6]

list_union = list_num_1 + list_num_2

print(list_union)