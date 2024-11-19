#3. Koristeći list comprehension, izgradite listu rječnika gdje su ključevi brojevi od 1 do 10, a vrijednosti
#kubovi tih brojeva, ali samo za neparne brojeve, za parne brojeve neka vrijednost bude sam broj:

"""kubovi = ...
print(kubovi) # [{1: 1}, {2: 2}, {3: 27}, {4: 4}, {5: 125}, {6: 6}, {7: 343}, {8: 8}, {9:
729}, {10: 10}]"""

kubovi = {n: n**3 if n % 2 != 0 else n for n in range(1, 11)}
print(kubovi)