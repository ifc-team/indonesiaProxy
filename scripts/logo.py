import colorama
import os

from colorama import Fore


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def pattern():
    colorama.init(autoreset=True)
    log = r"""
    ____                                _ ____    _   _ 
    |  _ \ _ __ ___  _   ____   __      | ||    \ | \ | |
    | |_) | '__/ _ \\ \ / /\ \ / / ____ | || |\  ||  \| |
    |  __/| | | (_) |> x <  \ v / |____|| || |/  /| |\  |
    |_|   |_|  \___//_/ \_\  / /        |_||____/ |_| \_|
    .:: Dev : @qorri-di ::. /_/  .:: ver : 0.0.1-Beta ::.                     
    """
    print(Fore.WHITE + log)


def logo():
    clear()
    pattern()
