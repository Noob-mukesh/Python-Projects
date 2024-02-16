import time 
#Mutiplication table using loop in python
print("Multiplication Table using python ")
def number_input():
    try:
        tb = int(input("enter any number : "))
    except ValueError:
        number_input()
    return tb
def play_more():
    Ask = input("want to play more?\nanswer Yes or No only : ")
    if "yes" in Ask.lower():
        print_table()
        play_more()
    else:
        print("Thnks for using my python code Join @Mr_sukkun for more ..")
   
def print_table():
    tb=number_input()
    start=time.time()
    i = 1
    print("Multiplication Table using while loop")
    while i <= 10:
        print(f"{tb} × {i} = {i * tb}")
        i += 1
    print(f"Time taken to complete {time.time()-start :2f}")
    print("Multiplication Table using for loop")
    start=time.time()
    for i in range(1, 11):
        print(f"{tb} × {i} = {i * tb}")
    print(f"Time taken to complete {time.time()-start :2f}")
print_table()
play_more()