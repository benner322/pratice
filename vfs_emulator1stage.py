import os, socket
import tkinter as tk

user = os.getenv("USER") or os.getenv("USERNAME") or "user"
host = socket.gethostname()
root = tk.Tk()
root.title("Терминал")
text = tk.Text(root)
text.pack()
entry = tk.Entry(root)
entry.pack(fill=tk.X)
def execute(event):
    a = entry.get()
    entry.delete(0, tk.END)
    text.insert(tk.END, f"{user}@{host}:~$ {a}\n")   
    b = a.split()
    if a == "exit":
        root.quit()
    elif b and b[0] == "ls":
        text.insert(tk.END, f"Команда: ls, аргументы: {b[1:]}\n")
    elif b and b[0] == "cd":
        text.insert(tk.END, f"Команда: cd, аргументы: {b[1:]}\n")
    elif b:
        text.insert(tk.END, f"Неизвестная команда: {b[0]}\n")   
    text.see(tk.END)

entry.bind("<Return>", execute)
text.insert(tk.END, f"Эмулятор - [{user}@{host}]\n")
entry.focus()
root.mainloop()
