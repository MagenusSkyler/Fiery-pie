import Fiery_pie as pie

print("Fiery-pie Interpreter [version - 1.0]", end="\n")
print("Help is unavailable for now.", end="\n\n")

while True:
    text = input("Fiery-pie >>> ")
    result, error = pie.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)
