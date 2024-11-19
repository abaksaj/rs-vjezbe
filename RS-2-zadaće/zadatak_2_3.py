#3. Koristeći odgovarajuću funkciju višeg reda i lambda izraz 
# (bez comprehensiona), pohranite u varijablu
# transform rezultat kvadriranja svih 
# brojeva u listi gdje rezultat mora biti rječnik gdje su ključevi
# originalni brojevi, a vrijednosti kvadrati tih brojeva:

"""brojevi = [10, 5, 12, 15, 20]
transform = ...
print(transform) # {10: 100, 5: 25, 12: 144, 15: 225, 20: 400}"""

# Lista brojeva
brojevi = [10, 5, 12, 15, 20]

# Stvara riječnik uz map i lambda funkciju
transform = dict(map(lambda x: (x, x**2), brojevi))

# Rezultat
print(transform)  #{10: 100, 5: 25, 12: 144, 15: 225, 20: 400}

