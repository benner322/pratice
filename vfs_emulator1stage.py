import os, socket

user = os.getenv("USER") or os.getenv("USERNAME") or "user"
host = socket.gethostname()
print(f"Эмулятор - [{user}@{host}]")

while True:
    a = input(f"{user}@{host}:~$ ")
    b = a.split()

    if a == "exit":
        print("Выход из эмулятора.")
        break

    if len(b) == 0:
        continue

    if b[0] == "ls":
        print(f"Команда: ls, аргументы: {b[1:]}")
        continue

    if b[0] == "cd":
        print(f"Команда: cd, аргументы: {b[1:]}")
        continue

    print(f"Неизвестная команда: {b[0]}")
