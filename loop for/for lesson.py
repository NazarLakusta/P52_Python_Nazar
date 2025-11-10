
# цикл з лічильником (range)
# i = 0 , i = 1  .....  n
for i in range(1,10):
    print(f"День № {i}")

# таблиця множення числа 5
for i in range(1,11):
    print(f"5 x {i} = {5*i}")

# відлік назад,  -1  крок
for i in range(10,0,-1):
    print(i)
print("Start")

# парні числа
for i in range(0,100,2):
    print(i)


# непарні числа
for i in range(1,100,2):
    print(i)


# сума чисел діапазноку
total = 0
for i in range (1,10):
    total += i

print(f"Сума від 1 до 10 - {total}")

# трикутник з зірочок
for i in range(1,6):
    print("*"*i)


# /////////////////////////////////
# цикл і списки
fruits = ["яблуко","банан","вишня","ківі"]

# показати елементи списка
for i in range(len(fruits)):
    print(f"Елемент №{i} - {fruits[i]}")


# показати елементи з парним номером індекса
for i in range(0,len(fruits),2):
    print(f"Елемент №{i} - {fruits[i]}")


for i in range(len(fruits)):
    fruits[i] = len(fruits[i])

print(fruits)


grades = [11,9,5,7,10,12]
for i in range(len(grades)):
    print(f"Студент №{i+1}: оцінка {grades[i]}")



word  = ["abcv","dsadsadsa","dsadas","dsadas","dsadasdas"]
word_6_len = []
for i in range(len(word)):
    if len(word[i]) > 6:
        print(word[i])
        word_6_len.append(word[i])


print(word_6_len)


i ** 2





