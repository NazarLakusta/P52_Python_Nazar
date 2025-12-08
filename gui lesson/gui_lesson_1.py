# підключити бібліотеку
import tkinter as tk

def change_text():
    # config - зммінити якийсь параметр
    if label["text"] == "Hello, TKInter":
        label.config(text="Hello, Nazar!")

    else:
        label.config(text="Hello, TKInter")


# створення самого вікна
root = tk.Tk()

# назва вікна
root.title("Моя перша ГУІ програма")

# розміри вікна
root.geometry("500x400+750+100")

# заблокувати зміну розміра
root.resizable(False,False)


label = tk.Label(root,text = "Hello, TKInter",
                 font = ("Arial",25,"bold"),  # шрифт - розмір - стиль
                 fg="white",  # - колі тексту
                 bg="black",  # - колір фону текста
                 padx=30,
                 pady=15
                 )
label.pack()

# створення кнопки
button = tk.Button(root, text = "Click ME",
                   font=("Arial",20),
                   fg="white",
                   bg="green",
                   width=10,
                   height=2,
                   relief="ridge", # стиль рамки: flat, raised,sunken, groove, ridge
                   command=change_text
                   )
button.pack()




# показати на екрані вікно
root.mainloop()


