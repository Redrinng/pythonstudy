import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen_var.set(result)
        except:
            screen_var.set("Error")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

root = tk.Tk()
root.title("Simple Calculator")

screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold")
screen.pack(fill=tk.X, ipadx=8, padx=10, pady=10)

buttons = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["0", "C", "="],
    ["+", "-", "*", "/"]
]

for row_values in buttons:
    frame = tk.Frame(root)
    frame.pack()
    for value in row_values:
        b = tk.Button(frame, text=value, font="lucida 15 bold", padx=20, pady=10)
        b.pack(side=tk.LEFT, padx=5, pady=5)
        b.bind("<Button-1>", click)

root.mainloop()
