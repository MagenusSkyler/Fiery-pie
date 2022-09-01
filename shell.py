import Fiery_pie as pie

print("Fiery-pie Interpreter [version - 1.0]", end="\n")
print("Type [help] or [/?] to get help.", end="\n\n")

while True:
    text = input("Fiery-pie >>> ")
    if text == "help" or text == "/?":
        print("Help is unavailable at this moment.")
        continue
    result, error = pie.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)
