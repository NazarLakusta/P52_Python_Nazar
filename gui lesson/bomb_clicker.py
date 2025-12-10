import tkinter as tk
bomb = 100 # timer
score = 0
press_return = True




root = tk.Tk()
root.title("Game")
root.geometry("600x600+750+400")
root.iconbitmap("img/bomb.ico")
root.resizable(False,False)


label = tk.Label(root, text = "Press[Enter] to start the game",
                 font=("Comic Sans MS",12))
label.pack()

fuse_label = tk.Label(root, text = f"Fuse: {str(bomb)}",
                      font=("Comic Sans MS",14))
fuse_label.pack()

score_label = tk.Label(root, text = f"Score: {str(score)}",
                      font=("Comic Sans MS",14))
score_label.pack()

img_1 = tk.PhotoImage(file="img/1.gif")
img_2 = tk.PhotoImage(file="img/2.gif")
img_3 = tk.PhotoImage(file="img/3.gif")
img_4 = tk.PhotoImage(file="img/4.gif")

bomb_label = tk.Label(image=img_1)
bomb_label.pack()

click_button = tk.Button(root,text = "Click me",
                         bg="black",
                         fg="white",
                         width=15,
                         font=("Comic Sans MS",14),
                         command=click)
click_button.pack()

root.bind("<Return>",start)



root.mainloop()