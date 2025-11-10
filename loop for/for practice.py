# квадрат
for i in range(1,11):
    print(f"{i}^2 = {i**2}")


for i in range(1,11):
    print(str(i)*i)
# 1
# 22
# 333
# 4444


password = ["1234","Abcd12121","abc","sadasd43223"]

for i in range(len(password)):
    if len(password[i]) >= 8:
        print(password[i]," - сильний")

    else:
        print(password[i], " - не сильний")



likes = [43,22,19,56,75]

average = sum(likes)/len(likes)
print(f"Average: {average}")

for i in range(len(likes)):
    if likes[i] > average:
        print(f"Популярний пост: №{i+1} - {likes[i]}")


days = ["Пн","Вт","Сд","Чт"]
plan = ["біг","зал","прес","йога"]


for i in range(len(days)):
    print(f"{days[i]} - тренування {plan[i]}")


