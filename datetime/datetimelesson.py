from datetime import date, time, datetime, timedelta

# дістати сьогоднішню дату
today = date.today()
print(today)

# створення кастомної дати
custom_date = date(2025,10,12)
print(custom_date)


# можна діставати частини дати
print(custom_date.year)
print(custom_date.month)
print(custom_date.day)


date_1 = date(2025,1,1)
date_2 = date(2025,2,10)
# порівняння дат
print(date_2 > date_1)




# створення часу
time_1 = time(14,30,15)
print(time_1)
print(time_1.hour)
print(time_1.minute)
print(time_1.second)

# створення дати і часу одночасно
date_time_1 = datetime(2025,10,12,14,45,0)

print(date_time_1.day, date_time_1.month, date_time_1.year)
print(date_time_1.hour, date_time_1.minute, date_time_1.second)

# дата і час в момент запуску програми
date_time_now = datetime.now()
print(date_time_now)

# перетворення дати у текст
date_to_str = date_time_now.strftime("%Y/%m/%d       %H:%M:%S")
print(date_to_str)

# перетворення з тексту в дату
str_1 = "2025-10-20 20:20"

str_to_date = datetime.strptime(str_1, "%Y-%m-%d %H:%M")
print(str_to_date)
print(str_to_date.year)



today = date.today()
# щоб додати до дати  дні, використомуємо timedelta
deadline = today + timedelta(days=30)
print(deadline)

# різниця дат

date_1 = date(2005,12,12)
difference_date = today - date_1
print(difference_date.days)




# номер дня тижня який вказаний у даті

print(today.isoweekday())

if today.isoweekday() == 3:
    print("Середа")


