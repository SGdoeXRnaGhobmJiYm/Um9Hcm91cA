from lib.controllers import Controller
from lib.arguments import parse_args
import multiprocessing


import os; os.system("clear")
print()
print('\rPremium v2.0\n')
print()
        
if __name__ == "__main__":
    multiprocessing.freeze_support()
    controller = Controller(
        arguments=parse_args()
    )
    try:
        controller.join_workers()
    except KeyboardInterrupt:
        pass
