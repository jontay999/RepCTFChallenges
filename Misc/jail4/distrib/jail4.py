#!/usr/local/bin/python3

flag = "REP{FAKE_FLAG}"
print("Okay you've probably had enough of pyjails, but last one I promise!")

# tiny payload....but at least you have the flag right?
MAX_CODE_SIZE = 20
try:
    if len(your_input := input("> ")) > MAX_CODE_SIZE: exit() # byee

    print(f"Okay, go ahead, your input is only {len(your_input)} characters long")
    
    # wait stop, why are you adding so many letters to the flag????
    eval(your_input, {"__builtins__": {"fffflag": flag }})
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

