#4. Koristeći funkcije all i map , 
#provjerite jesu li svi studenti punoljetni:

"""studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19},
{"ime": "Marko", "prezime": "Marković", "godine": 22},
{"ime": "Ana", "prezime": "Anić", "godine": 21},
{"ime": "Petra", "prezime": "Petrić", "godine": 13},
{"ime": "Iva", "prezime": "Ivić", "godine": 17},
{"ime": "Mate", "prezime": "Matić", "godine": 18}
]
svi_punoljetni = ...
print(svi_punoljetni) # False"""


# Lista studenata spremljena u riječnik
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
    {"ime": "Marko", "prezime": "Marković", "godine": 22},
    {"ime": "Ana", "prezime": "Anić", "godine": 21},
    {"ime": "Petar", "prezime": "Petrić", "godine": 17},
    {"ime": "Mate", "prezime": "Matić", "godine": 18},
]

# Provjera da li su studenti odrasli
svi_punoljetni = all(map(lambda student: student["godine"] >= 18, studenti))

# Rezultat
print(svi_punoljetni)  # False (Petar ima 17)