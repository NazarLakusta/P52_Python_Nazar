import tkinter as tk
import random

# ----------------- Налаштування вікна -----------------
window = tk.Tk()
window.title("Гра з квадратами")
window.geometry("300x300")

# ----------------- Поле гри -----------------
canvas = tk.Canvas(window, width=300, height=300, bg="white")
canvas.pack()

# ----------------- Рахунок -----------------
score = 0
score_label = tk.Label(window, text=f"Очки: {score}", font=("Arial", 12))
score_label.pack()

# ----------------- Функція створення квадрата -----------------
def create_square():
    global score
    # випадкові координати квадрата
    x1 = random.randint(0, 250)
    y1 = random.randint(0, 250)
    x2 = x1 + 50
    y2 = y1 + 50

    # створюємо квадрат на canvas
    square = canvas.create_rectangle(x1, y1, x2, y2, fill="blue")

    # функція видалення квадрата та додавання очок
    def remove_square(event):
        global score
        canvas.delete(square)
        score += 1
        score_label.config(text=f"Очки: {score}")

    # прив'язуємо натискання миші до квадрата
    canvas.tag_bind(square, "<Button-1>", remove_square)

# ----------------- Функція автоматичного появлення квадратів -----------------
def spawn_squares():
    create_square()
    window.after(1000, spawn_squares)  # кожну секунду з’являється новий квадрат

# ----------------- Запуск гри -----------------
spawn_squares()
window.mainloop()
