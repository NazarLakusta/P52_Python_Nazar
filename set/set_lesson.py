list_1 = ["Nazar","Nazar","Dima"]

print(list_1)

# перетворення з списку у множину
set_list = set(list_1)
print(set_list)

# спосіб створення
letters = set(["a","b","c","a"])

# пуста множина
empty_set = set()



fruits = {"apple","banana","orange"}
print(fruits)

# добавити один елемент
fruits.add("cherry")
print(fruits)

# добавити декілька елементів
fruits.update(["mango","kiwi","grape"])
print(fruits)


# видалення : remove - якщо немає - помилка
fruits.remove("mango")
print(fruits)

# видалення : discard - якщо немає - так і буде
fruits.discard("grape")
print(fruits)

# pop - видаляє рандомний елемент
fruits.pop()
print(fruits)

# clear - повністю очищує
fruits.clear()
print(fruits)



fruits = {"apple","banana","orange"}

# перевірити наявність елемента
print("apple" in fruits)
print("apple" not in fruits)



a = {1,2,3}
b = {3,4,5}

# обєднати |
c = a | b
print(c)

# перетин % спільне
print(a & b)

# різниця - що є в одному але нема в іншому
print(a - b)


# симетрична різниця ^ - В а або б , но не в обох
print(a ^ b)


# len - кількість елементів
# max() , min() , sum()







