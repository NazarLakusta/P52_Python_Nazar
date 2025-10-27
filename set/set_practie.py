monday = ["Nazar", "Vlad", "Sasha"]
tuesday = ["Sasha", "Pasha", "Nazar"]

#1.1
days = monday+tuesday
print(days)

set_people = set(days)
print(set_people)

# 1.2

monday_set = set(monday)
tuesday_set = set(tuesday)


print(f"Були і там і там: {monday_set & tuesday_set}")
print(f"У понеділок {monday_set}")


team_a = {"Nazar", "Sasha", "Vlad"}
team_b = {"Sasha", "Pasha", "Vlad"}


team = team_a | team_b
print(team)



print(team_a ^ team_b)
print(team_a & team_b)

list_1 = [5, 2, 3, 2, 1, 5, 4]
list_1.sort()
list_1_set = set(list_1)
print(list_1_set)



text = input("Введи якесь речення: ")

list_word = text.split(" ")
print(list_word)

word_set = set(list_word)
print(word_set)
print(f"Кількість унікальних слів: {len(word_set)}")



