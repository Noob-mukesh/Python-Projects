try:
    from colorama import Fore,Style,Back
except:
    import os
    os.system("pip install colorama")

n=input("Please enter your Name -> ")
class wish:
    """happy new year wishes class with different color output
     by @MR_sukkun
    """
    def __init__(self,name):
        self.name=name
    def __str__(self) -> str:
        return  f"Happy New Year, {self.name}"
x=wish(n)
COLOR=[Fore.BLACK,Fore.BLUE,Fore.CYAN,Fore.CYAN,Fore.GREEN,Fore.YELLOW,Fore.RED,Fore.WHITE,Fore.MAGENTA]
BACK=[Back.BLACK,Back.BLUE,Back.CYAN,Back.CYAN,Back.GREEN,Back.YELLOW,Back.RED,Back.WHITE,Back.MAGENTA]
STYLE=[Style.BRIGHT,Style.DIM,Style.NORMAL,Style.RESET_ALL]
for i in STYLE:
    print(i,x)
for i in COLOR:
    print(i,x)
for i in BACK:
    print(i,x)
