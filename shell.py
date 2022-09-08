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
            try:
                os.system('wine cmd')
            except:
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
        print("version        Shows Pandabear's interpreter version.")
        print('\nBuilt In Function: \n------------------')
        print('Clear()        Clears the screen and shows command output, "0".')
        print('Cls()          Clears the screen and shows command output, "0".')
        print('Input()        Takes user input and does not take any arguments.')
        print('Input_int()    Takes only "Int" input from user & does not take any args.')
        print('Is_int()       Returns "1" if the specified data type is "Integer".')
        print('               [e.g. Is_int(10), Is_int(VAR_name), Is_int("Hello!")]')
        print('Is_str()       Returns "1" if the specified data type is "String".')
        print('               [e.g. Is_str(10), Is_str(VAR_name), Is_str("Hello!")]')
        print('Is_list        Returns "1" if the specified variable type is "list".')
        print('               [e.g. Set a=[1,2]; Is_list(a) # This will return "1" ]')
        print('Is_func        Returns "1" if a function is specified else returns "0".')
        print('               [e.g. Is_func(fun) # Will return "1" if "fun" is function]')
        print('Math_pi        Returns default "math.pi" value, this is built in variable.')
        print('Print()        Prints "Str", "Var" & calculates mathematical expression.')
        print('               [e.g. Print("Hello!"), Print((5+5)*2), Print(VAR_name)]')
        print('Print_ret()    Returns print value as "String" in double quotes.')
        print('Run()          Runs specified file. [e.g. Run("example.pb")]')
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
