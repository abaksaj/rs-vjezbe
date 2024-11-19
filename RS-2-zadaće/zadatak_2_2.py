#2. Koristeći funkciju filter , filtrirajte samo brojeve koji su veći od 5:

"""brojevi = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]
veci_od_5 = ...
print(veci_od_5) # [21, 33, 45, 9, 10]"""

# Lista brojeva
brojevi = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]

# Filtriraj brojeve veće od 5
veci_od_5 = list(filter(lambda x: x > 5, brojevi))

# Ispisuje rezultat
print(veci_od_5)  # [21, 33, 45, 9, 10]