# IMPORTS
import os
import Pandabear as pbear

# ON START
if os.name == "nt":
    os.system("CLS && TITLE Pandabear")
print("Pandabear Interpreter [version - 1.0]", end="\n")
print("Type [help] or [/?] to get help.", end="\n\n")

# MAIN LOOP
while True:
    text = input("Pandabear >>> ")  # TAKE COMMAND INPUT
    
    # COMMAND INPUT CHECK FROM A - Z IN ASCENDING ORDER
    if text == "cls" or text == "clear":
        if os.name == "nt":
            os.system("cls")
            continue
        else:
            os.system("clear")
            continue
    elif text == "cmd":
        if os.name == "nt":
            os.system("cls && cmd")
        else:
            print("Cannot run 'cmd' unless running OS is Windows")
            continue
    elif text == "exit":
        break
    elif text == "help" or text == "/?":
        print('\nPandabear Shell commands: \n-------------------------')
        print('clear, cls     Clears the screen.')
        print('cmd            Opens Windows command prompt interpreter.')
        print('exit           Quits the Pandabear command interpreter.')
        print('help, /?       Provides Help information.')
        print('version        Shows Pandabear version.')
        print('\nBuilt In Function: \n------------------')
        print('CLEAR()        Clears the screen and shows output.')
        print('CLS()          Clears the screen and shows output.')
        print('Run()          Runs specified file [e.g. Run("example.pb")]')
        print("               Note: Do not use single quotes ('').")
        print(end="\n")     # ADD 1 LINE GAP AT THE END
        continue
    elif text == "version":
        print("Pandabear 1.0")
        continue
    
    # CALL MAIN INTERPRETER FUNCTIONS
    if text.strip() == "": continue
    result, error = pbear.run('<stdin>', text)

    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
