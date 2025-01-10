from typing import Callable
from colorama import Fore, Back, Style
from tkinter import filedialog
import tkinter as tk
import colorama
import datetime
import os
import sys

colorama.init(autoreset=True)
history_lst = []
path: str = str(os.getcwd()).replace("\\", "/")

clear: Callable[[], int] = lambda: os.system("cls")

if not os.path.exists('/TerminalLog'):
    os.makedirs("/TerminalLog")


def interface():
    print(f'''       
                        ▄████▄   ▒█████   ███▄ ▄███▓ ▒█████   ██▓     ██▓ ███▄    █ ▓█████ 
                        ▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▒██▒  ██▒▓██▒    ▓██▒ ██ ▀█   █ ▓█   ▀ 
                        ▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▒██░  ██▒▒██░    ▒██▒▓██  ▀█ ██▒▒███   
                        ▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ▒██   ██░▒██░    ░██░▓██▒  ▐▌██▒▒▓█  ▄ 
                        ▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒░ ████▓▒░░██████▒░██░▒██░   ▓██░░▒████▒
                        ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒░▓  ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░
                          ░  ▒     ░ ▒ ▒░ ░  ░      ░  ░ ▒ ▒░ ░ ░ ▒  ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░
                        ░        ░ ░ ░ ▒  ░      ░   ░ ░ ░ ▒    ░ ░    ▒ ░   ░   ░ ░    ░   
                        ░ ░          ░ ░         ░       ░ ░      ░  ░ ░           ░    ░  ░
                        ░ {Fore.BLUE}Terminal Software Made By @MHBASAMED {Fore.RED}<3                                                                          
''')
    return


def load_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory()
    return file_path


def mkdir(command):
    if command == "mkdir":
        print("The syntax of the command is incorrect.")
    else:
        lst = command.split(" ")
        for i in range(1, len(lst)):
            if "/" in lst[i]:
                os.makedirs(lst[i])
            else:
                os.mkdir(lst[i])
    return


def rmdir(command):
    if command == "rmdir":
        print("The syntax of the command is incorrect.")
    elif command == "rmdir -d":
        try:
            os.rmdir(load_file())
        except OSError:
            print("The directory is not empty")
    else:
        lst = command.split(" ")
        for i in range(1, len(lst)):
            try:
                if "/" in lst[i]:
                    os.removedirs(lst[i])
                else:
                    os.rmdir(lst[i])
            except FileNotFoundError:
                print(f"The system cannot find the file specified: '{lst[i]}'")
            except OSError:
                print(f"The directory is not empty: '{lst[i]}'")
    return


def pwd():
    file = open("/TerminalLog/LastCommand.txt", "w", encoding="UTF-8")
    file.write(path + "\n")
    file.close()
    return path


def ls():
    file = open("/TerminalLog/LastCommand.txt","w",encoding="UTF-8")
    for i in os.listdir():
        if os.path.isdir(i):
            print(str(str.zfill(str(os.path.getsize(i)), 10)) + "  [dir]   " + i)
            file.write(str(str.zfill(str(os.path.getsize(i)), 10)) + "  [dir]   " + i + "\n")
        elif os.path.isfile(i):
            print(str(str.zfill(str(os.path.getsize(i)), 10)) + "  [file]   " + i )
            file.write(str(str.zfill(str(os.path.getsize(i)), 10)) + "  [file]   " + i + "\n")
        elif os.path.islink(i):
            print(str(str.zfill(str(os.path.getsize(i)), 10)) + "  [Link]   " + i)
            file.write(str(str.zfill(str(os.path.getsize(i)), 10)) + "  [link]   " + i + "\n")
    file.close()
    return


def history():
    file = open("/TerminalLog/LastCommand.txt", "w", encoding="UTF-8")
    for i in range(len(history_lst)):
        if history_lst[i] != "":
            print(f"{i + 1}  {history_lst[i]}")
            file.write(f"{i + 1}  {history_lst[i]}" + "\n")
    file.close()
    return


def rmfile(command):
    if command == "rmfile":
        print("The syntax of the command is incorrect.")
    elif command == "rmfile -d":
        os.remove(load_file())
    else:
        lst = command.split(" ")
        for i in range(1, len(lst)):
            if lst[i] not in os.listdir() or os.path.isfile(lst[i]) == False:
                print(f"{lst[1]}: No such File")
            else:
                os.remove(lst[i])
    return


def touch(command):
    if command == "touch":
        print("The syntax of the command is incorrect.")
    else:
        lst = command.split(" ")
        for i in range(1, len(lst)):
            open(f"{lst[i]}", "a")


def cd(command):
    global path
    if command == "cd -d":
        path = load_file()
        os.chdir(path)
    elif len(command.split()) == 2:
        lst = command.split()
        try:
            os.chdir(lst[1])
            path = str(os.getcwd()).replace('\\', '/')
        except FileNotFoundError:
            print("The system cannot find the file specified")
    else:
        print("The syntax of the command is incorrect.")


def cp(command):
    if command == "cp":
        print("The syntax of the command is incorrect.")
    else:
        lst = command.split(" ")
        os.system(f"copy {lst[1]} {lst[2]}")


def mv(command):
    if command == "mv":
        print("The syntax of the command is incorrect.")
    else:
        lst = command.split(" ")
        os.system(f"move {lst[1]} {lst[2]}")

def date_time():
    file = open("/TerminalLog/LastCommand.txt","w",encoding="UTF-8")
    file.write(str(datetime.datetime.now()) + "\n")
    file.close()
    return datetime.datetime.now()

def cat(command):
    if command == "cat":
        print("The syntax of the command is incorrect.")
    else:
        lst = command.split()
        with open(lst[1],"r",encoding="utf-8") as file:
            for i in file:
                print(i.strip())

def pcl():
    file = open("/TerminalLog/LastCommand.txt","w",encoding="UTF-8")
    file.write(str(os.getlogin()) + "\n")
    file.close()
    return os.getlogin()


commands = {
    "pcl" : pcl,
    # "cat": cat
    # "cd": cd,
    # "cp": cp,
    # "clear": clear,
    "datetime" : date_time,
    "pwd": pwd,
    "ls": ls,
    # "mkdir": mkdir,
    "history": history
    # "rmdir": rmdir,
    # "rmfile": rmfile,
    # "touch": touch,
    # "mv": mv
    # "help" : help
}
def write_append(command):
    if command.startswith(" ") or command.startswith(">"):
        print("The syntax of the command is incorrect.")
    elif " > " in command:
        lst = command.split(" ")
        if lst[0] in commands:
            x = commands[lst[0]]
            x()
            open(f"{path}/{lst[2]}","w",encoding="utf-8").writelines(open(f"/TerminalLog/LastCommand.txt","r",encoding="utf-8").readlines())
    elif " >> " in command:
        lst = command.split(" ")
        if lst[0] in commands:
            x = commands[lst[0]]
            x()
            open(f"{path}/{lst[2]}","a",encoding="utf-8").writelines(open(f"/TerminalLog/LastCommand.txt","r",encoding="utf-8").readlines())


interface()

def Main():
    c = input(str(path) + ">")
    history_lst.append(c)

    if c == "clear":
        clear()
        interface()

    elif c == "pwd":
        print(pwd())

    elif c == "ls":
        ls()

    elif c.startswith("mkdir"):
        mkdir(c)

    elif c == "history":
        history()

    elif c.startswith("rmdir"):
        rmdir(c)

    elif c.startswith("rmfile"):
        rmfile(c)

    elif c.startswith("touch"):
        touch(c)

    elif c.startswith("cd"):
        cd(c)

    elif c.startswith("cp"):
        cp(c)

    elif c.startswith("mv"):
        mv(c)
    elif c == "datetime":
        print(date_time())

    elif c.startswith("cat"):
        cat(c)

    elif c == "pcl":
        print(pcl())

    elif " > " in c or " >> " in c:
        write_append(c)
        clear()
        interface()

    elif c == "help":
        print("""
        
This Terminal Software Made By @MHBASAMED
pcl         Print current user login.
cat         See the content of the file :: cat [file|path file]
cd          Change directory :: cd [-d][path][/][./][../]
cp          Copies files from one place to another :: cp [file|path file] [path]
clear       Clear the terminal.
datetime    Print the current date and time.
pwd         Print working directory.
ls          List directory files :: ls [path]
mkdir       Make directory :: mkdir [dirs(n)|path]
history     History of commands.
rmdir       Remove directory :: rmdir [-d] [dirs(n)|path]
rmfile      Remove file :: rmfile [-d] [files(n)|path]
touch       Make file :: touch [name|path]
mv          Move file or directory :: mv [name|path] [name|path]
>           Write the result of the command to file :: [command] > [name|path]
>>          Append the result of the command to file :: [command] > [name|path]
help        help menu.
""")

if __name__ == '__main__':
    while True:
        Main()

