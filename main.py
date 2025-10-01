import getpass
import socket

class ShellEmulator:
    def __init__(self):
        self.vfs_name = "my_vfs"
        self.running = True
        
    def parse_arguments(self, command_line):
        """Парсер, который корректно обрабатывает аргументы в кавычках"""
        args = []
        current_arg = ""
        in_quotes = False
        
        for char in command_line:
            if char == '"':
                in_quotes = not in_quotes
            elif char == ' ' and not in_quotes:
                if current_arg:
                    args.append(current_arg)
                    current_arg = ""
            else:
                current_arg += char
                
        if current_arg:
            args.append(current_arg)
            
        return args
    
    def display_prompt(self):
        """Отображает приглашение к вводу"""
        username = getpass.getuser()
        hostname = socket.gethostname()
        print(f"Эмулятор - [{username}@{hostname}] {self.vfs_name}$ ", end="")
    
    def handle_ls(self, args):
        """Обработчик команды ls (заглушка)"""
        print(f"ls вызвана с аргументами: {args}")
    
    def handle_cd(self, args):
        """Обработчик команды cd (заглушка)"""
        print(f"cd вызвана с аргументами: {args}")
    
    def handle_exit(self, args):
        """Обработчик команды exit"""
        print("Завершение работы эмулятора...")
        self.running = False
    
    def execute_command(self, command_line):
        """Выполняет введенную команду"""
        args = self.parse_arguments(command_line)
        if not args:
            return
            
        command = args[0]
        arguments = args[1:]
        
        # Обработка команд
        if command == "exit":
            self.handle_exit(arguments)
        elif command == "ls":
            self.handle_ls(arguments)
        elif command == "cd":
            self.handle_cd(arguments)
        else:
            print(f"Ошибка: команда '{command}' не найдена")
    
    def run(self):
        """Основной цикл программы"""
        print("Эмулятор командной строки запущен")
        print("Доступные команды: ls, cd, exit")
        print("Для выхода введите 'exit'")
        print("-" * 50)
        
        while self.running:
            try:
                self.display_prompt()
                command_line = input().strip()
                
                if command_line:
                    self.execute_command(command_line)
                    print()  # Пустая строка для читабельности
                    
            except KeyboardInterrupt:
                print("\nЗавершение работы...")
                break
            except EOFError:
                print("\nЗавершение работы...")
                break

if __name__ == "__main__":
    emulator = ShellEmulator()
    emulator.run()