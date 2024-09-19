#!/usr/local/bin/python3

flag = "REP{t3ll_m3_h0w_y0u_d1d_IT_pls_1337}"
length = len(flag)
flag1, flag2 = flag[:length//2], flag[length//2:]

def part1():
    print("a tiny payload....but at least you have the flag right?")
    MAX_CODE_SIZE = 20
    try:
        if len(your_input := input("> ")) > MAX_CODE_SIZE: exit() # byee

        print(f"Okay, go ahead, your input is only {len(your_input)} characters long")
        
        # wait stop, why are you adding so many letters to the flag????
        eval(your_input, {"__builtins__": {"fffflag": flag1 }})
    except:
        pass

    print("Anywayy, I found some random flags in some of python's types")
    print("Int:", int.__flags__)
    print("Float:", float.__flags__)
    print("Bool:", bool.__flags__)
    print("Str:", str.__flags__)
    print("Tuple:", tuple.__flags__)
    print("List:", list.__flags__)

    print("Strange numbers...I'm sure there's good documentation for that somewhere")
    print("...right?")

def part2():
    MAX_CODE_SIZE = 25
    try:
        if len(your_input := input("> ")) > MAX_CODE_SIZE: exit() # byee
        
        print(f"Okay, go ahead, your input is only {len(your_input)} characters long")
        print("Oh no i'm blind")
        
        import sys
        sys.stdout = None 
        sys.stderr = None
        sys.stdin = None

        eval("".join(reversed(your_input)), {"__builtins__": {"galf": flag2[::-1], "rr": reversed}})
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        sys.stdin = sys.__stdin__

        print("oh wait i can see now, all's good")
    except:
        pass

def menu():
    print("Okay you've probably had enough of pyjails, but last one I promise!")
    print("This was supposed to be 2 challenges, but I mashed them into one")
    print("With luck, the difficulty of this challenge will force you to actually do some easier pwn challenges... ")
    print("(unless you're from TomatoFans, uhm in that case, good luck...)")
    MENU  = "\n====================  Menu ====================\n"
    MENU += "Select:\n"
    MENU += " 1. Try your hand at part 1 where I use weird python stuff \n"
    MENU += " 2. Try your hand at part 2 where I do everything backwards \n"
    MENU += "> "
    choice = input(MENU)
    return choice

if __name__ == "__main__":
    try:
        choice = menu()
        if choice == "1":
            part1()
        elif choice == "2":
            part2()
    except :
        exit()
