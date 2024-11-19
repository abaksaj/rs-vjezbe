import random

target = random.randint(1, 100)
pogodak = None

while pogodak != target:
    pogodak = int(input(" Pogodite broj između 1 i 100: "))
    if pogodak < target:
        print("Broj je ispod 1!")
    elif pogodak > target:
        print("Broj je iznad 100!")
    else:
        print("Pogodili ste pravi broj!")5