import tkinter as tk
from tkinter import messagebox

def check_winner():
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if bottons[combo[0]]["text"] == bottons[combo[1]]["text"] and bottons[combo[1]]["text"] == bottons[combo[2]]["text"]:
            bottons[combo[0]].config(bg="green")
            bottons[combo[1]].config(bg="green")
            bottons[combo[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"player{bottons[combo[0]]['text']} wins")
            root.quit()
            return

    
    if all(bottons[i]["text"]!= "" for i in range(9)):
        messagebox.showinfo("Tic-Tac-Toe", "The game is a tie")
        root.quit()
        return

def botton_cilck(index):
    if bottons[index]["text"]=="" and not winner:
        bottons[index]["text"] = curent_player
        check_winer()
        toggle_player()

def toggle_player():
    global curent_player
    curent_player = "x" if curent_player == "o" else "o"
    lable.config(text=f"player{curent_player}'s turn")

root = tk.Tk()
root.title("Tic-Tac-Toe")

bottons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: botton_cilck(i)) for i in range(9)]

for i, button in enumerate(bottons):
    button.grid(row=i//3, column=i%3)

curent_player = "x"
winner = False
lable = tk.Label(root, text=f"player {curent_player}'s turn", font=("normal", 16))
lable.grid(row=3, column=0, columnspan=3)

root.mainloop()