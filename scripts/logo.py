import random, colorama, os
from colorama import Fore


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[0;33m'
    FAIL = '\033[91m'
    colors = [OKGREEN, FAIL, WARNING]
    RAND = random.choice(colors)


def pattern():
    colorama.init(autoreset=True)
    log = r"""
     ____                                _  ___   _   _ 
    |  _ \ _ __ ___  _   ____   __      | ||   \ | \ | |
    | |_) | '__/ _ \\ \ / /\ \ / / ____ | || |\ \|  \| |
    |  __/| | | (_) |> x <  \ v / |____|| || |/ /| |\  |
    |_|   |_|  \___//_/ \_\  / /        |_||___/ |_| \_|
                            /_/                       
    """
    print(Fore.WHITE + log)
    print(bcolors.OKGREEN + '+------------------------------------------------------------+')
    print(bcolors.WARNING + '|           .:.: Dev: https://qorrri-di.com :.:.             |')
    print(bcolors.WARNING + '|           .:.: Ver:                                        |')
    print(bcolors.OKGREEN + '+------------------------------------------------------------+')


def logo():
    clear()
    pattern()
