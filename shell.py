# IMPORTS
import os
import Pandabear as pbear

# ON START
os.system("TITLE Pandabear")
print("Pandabear Interpreter [version - 1.0]", end="\n")
print("Type [help] or [/?] to get help.", end="\n\n")

# MAIN LOOP
while True:
    text = input("Pandabear >>> ")  # TAKE COMMAND INPUT
    
    # COMMAND INPUT CHECK FROM A - Z IN ASCENDING ORDER
    if text == "clear":
        if os.name == "nt":
            os.system("cls")
            continue
        else:
            os.system("clear")
            continue
    elif text == "exit":
        break
    elif text == "help" or text == "/?":
        print("clear        Clears the screen.")
        print("exit         Quits the Pandabear program (command interpreter).")
        print("help, /?     Provides Help information.")
        print("version      Shows Pandabear version.")
        print(end="\n")     # ADD 1 LINE GAP AT THE END
        continue
    elif text == "version":
        print("Pandabear 1.0")
        continue
    
    # CALL MAIN INTERPRETER FUNCTIONS
    result, error = pbear.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)
