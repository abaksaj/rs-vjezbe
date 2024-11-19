#5. Definirajte varijablu min_duljina koja će pohranjivati int . Koristeći odgovarajuću funkciju višeg reda
#i lambda izraz, pohranite u varijablu duge_rijeci sve riječi iz liste rijeci koje su dulje od
#min_duljina :

"""rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
"pjesma", "otorinolaringolog"]
min_duljina = prompt("Unesite minimalnu duljinu riječi: ")
# min_duljina = 7
duge_rijeci = ...
# print(duge_rijeci) # ['zvijezda', 'prijatelj', 'čokolada', 'otorinolaringolog']"""

# Lista riječi
rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"]

# Min. duljina
min_duljina = 7  

# Riječi dulje od min.duljine
duge_rijeci = list(filter(lambda x: len(x) > min_duljina, rijeci))

# Rezultat
print(duge_rijeci)  
# ['zvijezda', 'prijatelj', 'čokolada', 'otorinolaringolog']


