'''Definirajte korutinu koja će simulirati dohvaćanje podataka s weba. 
Podaci neka budu lista brojeva od 1 do 10 koju ćete vratiti nakon 3 sekunde. 
Listu brojeva definirajte comprehensionom. Nakon isteka vremena, u korutinu ispišite poruku "Podaci dohvaćeni." i vratite podatke. 
Riješite bez korištenja asyncio.gather() i asyncio.create_task() funkcija.'''

import asyncio

async def dohvati(): # definicija asinkrone korutine dohvati()
    
    brojevi = [i for i in range(1,11)] #lista brojeva od 1 - 11, ide do 10
    await asyncio.sleep(3) # vraća brojeve nakon 3sek
    print("Podaci dohvaćeni.") # ispišite poruku "Podaci dohvaćeni."
    return brojevi # vratite podatke

async def brojevi(): # druga korutina koja awaita prvu korutinu i sprema ju u podaci te se sve ispusuje
    podaci = await dohvati() # pričekamo sa ispisom podataka
    print("Dohvaćeni podaci", podaci) # ispis podataka tj. liste
    
asyncio.run(brojevi()) # naredba pokreće korutinu
      

