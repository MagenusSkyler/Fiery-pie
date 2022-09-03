import Pandabear as pbear

print("Pandabear Interpreter [version - 1.0]", end="\n")
print("Type [help] or [/?] to get help.", end="\n\n")

while True:
    text = input("Pandabear >>> ")
    if text == "help" or text == "/?":
        print("Help is unavailable at this moment.")
        continue
    result, error = pbear.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)
