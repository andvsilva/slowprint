import random
import sys
import time
import os

# To print colored text in python 
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED   = "\033[1;31m"


time.sleep(10)

print()


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(random.random() * 0.2)


slowprint(f'{bcolors.WARNING}Aulas Particulares de Física e Matemática.{bcolors.ENDC}')
print()
slowprint(f'         {bcolors.FAIL}Professor André{bcolors.ENDC}')
slowprint('                                       TELEFONE:  19 9 8165-0211')
print()
slowprint('Método de ensino simples, rápido e eficiente. :)')
slowprint('Resolução comentada de listas de exercícios.')
print()
slowprint(f'{bcolors.OKBLUE}Especialidades:{bcolors.ENDC}')
slowprint(f'{bcolors.OKCYAN}-> Física{bcolors.ENDC}')
slowprint(f'{bcolors.RED}-> Matemática{bcolors.ENDC}')
slowprint(f'{bcolors.OKGREEN}-> Programação Geral:{bcolors.ENDC}')
slowprint('   -> C++, C')
slowprint('   -> Python')
slowprint('   -> Data Science')
slowprint('   -> Machine Learning')
slowprint('   -> Linux')
slowprint('   -> Git')

print()
slowprint('TELEFONE:  19 9 8165-0211')

time.sleep(10)
