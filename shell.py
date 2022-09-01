import Fiery_pie as pie

while True:
    text = input("Fiery-pie >>> ")
    result, error = pie.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)
