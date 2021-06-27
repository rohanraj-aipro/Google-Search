import colorama
from colorama import Fore, Back, Style
print(Fore.GREEN, Back.BLACK + '''''


__      __   _             ___                    
\ \    / /__| |__ ___ ___ / __|__ _ _  _ __ _ ___ 
 \ \/\/ / -_) '_ \___|___| (_ / _` | || / _` / -_)
  \_/\_/\___|_.__/        \___\__,_|\_,_\__, \___|
                                        |___/     
''''')
print(Fore.YELLOW, Back.BLACK + '   | |___________________________________________________| |')
print(Fore.YELLOW, Back.BLACK + '   | |_____________________________________________________)')
print(Fore.YELLOW, Back.BLACK + '   | |_____________________________________________________)')
print(Fore.YELLOW, Back.BLACK + '   | |          Made By:-  Hacker--Rohan Raj             | |')
print(Fore.YELLOW, Back.BLACK + '   | |                     Web-Gauge                     | |')
print(Fore.YELLOW, Back.BLACK + '   | |              Web - OSINT Tool                     | |')
print(Fore.YELLOW, Back.BLACK + '   | |     Search in Google without  Opening Google      | |')
print(Fore.YELLOW, Back.BLACK + '   | | Search in Google without Having google Installed  | |')
print(Fore.YELLOW, Back.BLACK + '   | |   Note:- This Tool Requires Internet Connection   | |')
print(Fore.YELLOW, Back.BLACK + '   | |___________________________________________________| |')
print(Fore.YELLOW, Back.BLACK + '   | |___________________________________________________| |')
print(Fore.YELLOW, Back.BLACK + '   | |---------------------------------------------------| |')


try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' \n Try Command pip3 install google \n or \n pip install google ")

# to search
query = input("What do You want to Search For ?\n")

for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)
