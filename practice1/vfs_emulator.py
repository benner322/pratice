import os
import socket
import tkinter as tk
import argparse
import sys
from xml.etree.ElementTree import Element, SubElement, tostring

# Парсинг аргументов
parser = argparse.ArgumentParser()
parser.add_argument('--vfs_path', default='./vfs')
parser.add_argument('--log_path', default='./log.xml') 
parser.add_argument('--script_path')
args = parser.parse_args()

print(f"VFS: {args.vfs_path}")
print(f"LOG: {args.log_path}")
print(f"SCRIPT: {args.script_path}")

# Логирование
class Logger:
    def __init__(self, path):
        self.path = path
        self.root = Element('log')
        
    def log(self, cmd, args, error=""):
        event = SubElement(self.root, 'event')
        SubElement(event, 'command').text = cmd
        SubElement(event, 'arguments').text = str(args)
        if error:
            SubElement(event, 'error').text = error
            
        with open(self.path, 'w') as f:
            f.write(tostring(self.root, encoding='unicode'))

logger = Logger(args.log_path)

# Выполнение скрипта
if args.script_path:
    try:
        with open(args.script_path) as f:
            for line in f:
                cmd = line.strip()
                if cmd and not cmd.startswith('REM'):
                    print(f"$ {cmd}")
                    # Здесь будет обработка команд
    except Exception as e:
        print(f"Ошибка скрипта: {e}")
        sys.exit(1)

# GUI
user = os.getenv("USER") or os.getenv("USERNAME") or "user"
host = socket.gethostname()

root = tk.Tk()
root.title(f"Эмулятор - [{user}@{host}]")
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
        logger.log("ls", b[1:])
    elif b and b[0] == "cd":
        text.insert(tk.END, f"Команда: cd, аргументы: {b[1:]}\n")
        logger.log("cd", b[1:])
    elif b:
        text.insert(tk.END, f"Неизвестная команда: {b[0]}\n")
        logger.log(b[0], b[1:], f"Неизвестная команда: {b[0]}")
    
    text.see(tk.END)

entry.bind("<Return>", execute)
text.insert(tk.END, f"Эмулятор - [{user}@{host}]\n")
entry.focus()
root.mainloop()
