#Zadatak 2: Funkcije višeg reda

#Definirajte sljedeće izraze korištenjem funkcija višeg reda i 
# lambda izraza:
"1. Koristeći funkciju map , kvadrirajte duljine svih nizova u listi:"

"""nizovi = ["jabuka", "kruška", "banana", "naranča"]
kvadrirane_duljine = ...
print(kvadrirane_duljine) # [36, 36, 36, 49]"""

# Lista stringova
nizovi = ["jabuka", "kruška", "banana", "naranča"]

# Računa kvadratne duljine
kvadrirane_duljine = list(map(lambda x: len(x)**2, nizovi))

# Ispisuje rezultat
print(kvadrirane_duljine)  # [36, 36, 36, 49]