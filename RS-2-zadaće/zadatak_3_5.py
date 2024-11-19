# 5. Koristeći list comprehension, izgradite listu rječnika gdje su ključevi prezimena studenata, 
# a vrijednosti
#su zbrojeni bodovi, iz liste studenti :

"""studenti = [
{"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
{"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
{"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
{"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
{"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
{"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]}
]
zbrojeni_bodovi = ...
print(zbrojeni_bodovi) # [{'Ivić': 152}, {'Marković': 127}, {'Anić': 55}, {'Petrić': 362},
{'Ivić': 236}, {'Matić': 266}]"""

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 54, 64]},
    {"ime": "Marko", "prezime": "Marković", "bodovi": [13, 15, 14, 45]},
    {"ime": "Ana", "prezime": "Anić", "bodovi": [18, 9, 4, 23, 111]},
    {"ime": "Petar", "prezime": "Petrić", "bodovi": [10, 57, 67, 77, 94, 98]},
    {"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
    {"ime": "Mateo", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 231]},
]

brojeni_bodovi = {student["prezime"]: sum(student["bodovi"]) for student in studenti}
print(brojeni_bodovi)