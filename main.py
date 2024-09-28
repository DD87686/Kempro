import time
import os
import pystyle
from pystyle import *
import yaml
def Tutorial(prompt):
    if DataStr.__contains__("'Tutorial': True"):
        if prompt == "ID":
            print(f"The '{pystyle.Colors.cyan}ID{pystyle.Colors.reset}' is the number in the link, copy and paste it here or just put the ID:")
        if prompt == "MDP":
            print(f"{pystyle.Colors.red}'MDP'{pystyle.Colors.reset} stands for {pystyle.Colors.red}'Max Download Parallel'{pystyle.Colors.reset}, and you decide how many posts you want to download at once. keep it below 15.")
        if prompt == "Proxy":
            print(f"{pystyle.Colors.reset}if you have a {pystyle.Colors.red}'proxy'{pystyle.Colors.reset} copy it here, if not {pystyle.Colors.red}'just press enter without putting in anything'{pystyle.Colors.reset}")

def Cls():
    os.system('cls' if os.name == 'nt' else 'clear')
def Logo():
    Logo = """
██╗  ██╗███████╗███╗   ███╗██████╗ ██████╗  ██████╗ 
██║ ██╔╝██╔════╝████╗ ████║██╔══██╗██╔══██╗██╔═══██╗
█████╔╝ █████╗  ██╔████╔██║██████╔╝██████╔╝██║   ██║
██╔═██╗ ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██╔══██╗██║   ██║
██║  ██╗███████╗██║ ╚═╝ ██║██║     ██║  ██║╚██████╔╝
╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ 
    """
    print(Center.Center(Logo))
with open('settings.yaml', 'r') as f:
    data = yaml.full_load(f)
    DataStr = f"{data}"
if DataStr.__contains__("'Logo': True"):
    Logo()
    time.sleep(2)
    Cls()
if DataStr.__contains__("'FirstLaunch': True"):
    with open('settings.yaml', 'r') as file:
        filedata = file.read()
        filedata = filedata.replace("FirstLaunch: True", "")
    with open('settings.yaml', 'w') as file:
        file.write(filedata)
    print(f"""Hello, welcome to {pystyle.Colors.red}KEMPRO{pystyle.Colors.reset}!
I can see that you launched this program for {pystyle.Colors.pink}the first time!{pystyle.Colors.reset}
You can change the settings in the '{pystyle.Colors.red}settings.yaml{pystyle.Colors.reset}' file.
This program is for scraping from kemono.su {pystyle.Colors.yellow}[PATREON CREATORS ONLY] {pystyle.Colors.gray}(hence the name){pystyle.Colors.reset}
To start this program, please relaunch it, thank you!!\n""")
    input("Press enter to relaunch...")
    os.system('start cmd /wait /c main.bat')
    exit()
if DataStr.__contains__("'Tutorial': True"):
    print(f"Welcome to KEMPRO!\nThis program is going to simply ask you for some stuff to get the kemono scraper running.\nYou can disable this tutorial/guide in the '{pystyle.Colors.red}settings.yaml{pystyle.Colors.reset}' file")
    print("\r(5)", end="")
    time.sleep(1)
    print("\r(4)", end="")
    time.sleep(1)
    print("\r(3)", end="")
    time.sleep(1)
    print("\r(2)", end="")
    time.sleep(1)
    print("\r(1)", end="")
    time.sleep(1)
    Cls()
Tutorial("ID")
uID = input(f"{pystyle.Colors.pink}ID: {pystyle.Colors.green}")
Tutorial("MDP")
MDP = input(f"{pystyle.Colors.pink}MDP: {pystyle.Colors.green}")
if MDP == str:
    print(f"{pystyle.Colors.red}Invalid Syntax: [String ≠ Integer]{pystyle.Colors.reset}")
    time.sleep(3)
    exit()
if int(MDP) >= 15:
    print(f"{pystyle.Colors.red}Invalid Syntax: [Integer isn't under 15 which is the maximal number]{pystyle.Colors.reset}")
    time.sleep(3)
    exit()
Tutorial("Proxy")
Proxy = input(f"{pystyle.Colors.pink}[OPTIONAL] Proxy: {pystyle.Colors.green}")
def Wriet():
    file = open(f'Kemonoscrapermaster\main\main.bat', 'w+')
    Write = f"""cd %cd%\Kemonoscrapermaster\main
    main.exe -link "https://kemono.su/patreon/user/{uID}" -async -max-download-parallel {MDP} """
    file.write(Write)
    os.system('start cmd /wait /k Kemonoscrapermaster\main\main.bat')
Wriet()
input("Press enter to close...")