#2. Koristeći list comprehension, izgradite listu duljina svih nizova u listi rijeci , ali samo za nizove koji
#sadrže slovo a :

"""rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
"pjesma", "otorinolaringolog"]
duljine_sa_slovom_a = ...
print(duljine_sa_slovom_a) # [6, 3, 6, 8, 9, 8, 6, 17]"""

rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
"pjesma", "otorinolaringolog"]

duljine_sa_slovom_a = [len(word) for word in rijeci if 'a' in word]

print(duljine_sa_slovom_a)