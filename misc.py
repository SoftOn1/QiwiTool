import os

from termcolor import colored

ban_account_desc = """Способ бана заключается в том, чтобы сделать как можно больше переводов на аккаунт жертвы
QIWI сочтет это за подозрительные переводы и забанит аккаунт.
Для лучшего эффекта можно переводить с комментариями "за соль", "за меф" и т.п

""" + colored("РАБОТОСПОСОБНОСТЬ НЕ ГАРАНТИРОВАНА!!", "red")

authors = colored("""Авторы данного скрипта:
(@BeanD_TM , @myfatcock""")



import webbrowser as wb
import colorama
import time
import random
from time import sleep
from colorama import init, Fore
init(autoreset=True)
if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")

print(Fore.GREEN + "  ______       __    __   __    ______  __  ___   ______       __  ____    __    ____  __  ")
print(Fore.GREEN + " /  __  \     |  |  |  | |  |  /      ||  |/  /  /  __  \     |  | \   \  /  \  /   / |  | ")
print(Fore.GREEN + "|  |  |  |    |  |  |  | |  | |  ,----'|  '  /  |  |  |  |    |  |  \   \/    \/   /  |  | ")
print(Fore.GREEN + "|  |  |  |    |  |  |  | |  | |  |     |    <   |  |  |  |    |  |   \            /   |  | ")
print(Fore.GREEN + "|  `--'  '--. |  `--'  | |  | |  `----.|  .  \  |  `--'  '--. |  |    \    /\    /    |  | ")
print(Fore.GREEN + " \_____\_____\ \______/  |__|  \______||__|\__\  \_____\_____\|__|     \__/  \__/     |__| ")
                                                                                           
print(" ====░=====░=====░==░=░======░=░=====░=====░==")
print("  Сделанна: ",   Fore.CYAN +   "@BeanD_TM      ")
print("  Обновления: ", Fore.CYAN +   "https://t.me/TreeSoft")
print(" =============================================")

def print_banner(count):
    os.system("cls")
    
    print(banner)
        
    print()
    print(f"Количество аккаунтов: {count}")
    print()

def menu(count):
    
    ch = input("> ")
    print_banner(count)
    
    return ch
