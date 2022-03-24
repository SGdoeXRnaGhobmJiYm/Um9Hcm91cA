from lib.controllers import Controller
from lib.arguments import parse_args
from colorama import Fore
import multiprocessing, requests, time, pyfiglet
fe = open("proxies.txt", "a")
be = open("proxies.txt", "w")
txt = pyfiglet.figlet_format(text="Sprites Tools!")
print(f' {Fore.LIGHTGREEN_EX}{txt}\n')
print(f' {Fore.RED}[+] Loading Program...\n')

if __name__ == "__main__":
    multiprocessing.freeze_support()
    controller = Controller(
        arguments=parse_args()
    )
    try:
        controller.join_workers()
    except KeyboardInterrupt:
        pass
        
