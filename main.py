import time
from rich import print
import os
import platform

PLATFORM_NAME = platform.system()
RESTARTED = False
commands = {"shutdown": "Shutdowns operating system",
            "restart": "Restarts operating system",
            "path": "Shows in which directory you are",
            "help": "Prints commands and their description",
            "time": "Shows datetime",
            "ps": "Shows active processes"}


def start():
    global RESTARTED
    print("[bold bright_yellow]Starting OS...[/bold bright_yellow]")
    time.sleep(0.5)
    print("[bold blue]OS Started Successfully![/bold blue]")
    time.sleep(0.5)
    user = input("Enter your name: ")

    while True:
        print(f"[bold green]{user}@root[/bold green] -->", end=' ')
        command = input()
        if command == "shutdown":
            print("System will [bold red]shutdown[/bold red] after 5 seconds...")
            time.sleep(5)
            print("System is shutdowning...")
            time.sleep(1)
            break

        elif command == "path":
            print(os.getcwd())

        elif command == "restart":
            print("System will [bold cyan]restart[/bold cyan] after 5 seconds...")
            time.sleep(5)
            print("[bold red]System is restarting...")
            time.sleep(1)

            if PLATFORM_NAME == "Windows":
                os.system("cls")
            elif PLATFORM_NAME == "Linux" or PLATFORM_NAME == "Darwin":
                os.system("clear")
            RESTARTED = True
            break

        elif command == "help":
            for key in commands.keys():
                print("  [bold blue]" + key + "[/bold blue]" + " --- " + commands[key])

        elif command == "time":
            print("  [bold #d78700]Local time: [/bold #d78700]" + time.ctime(time.time()))

        elif command == "ps":
            if PLATFORM_NAME == "Windows":
                os.system("tasklist")

            elif PLATFORM_NAME == "Linux" or PLATFORM_NAME == "Darwin":
                os.system("ps aux")

        elif command == "" or command == " ":
            pass

        else:
            print(f"[bold red]Incorrect command: {command}")

    if RESTARTED:
        RESTARTED = False
        start()


if __name__ == "__main__":
    start()
