'''2. Definirajte dvije korutine koje će simulirati dohvaćanje podataka s weba. 
Prva korutina neka vrati listu proizvoljnih rječnika (npr. koji reprezentiraju 
podatke o korisnicima) nakon 3 sekunde, a druga
korutina neka vrati listu proizvoljnih rječnika 
(npr. koji reprezentiraju podatke o proizvodima) nakon 5
sekundi. Korutine pozovite konkurentno korištenjem asyncio.gather() 
i ispišite rezultate. Program se mora izvršavati ~5 sekundi.'''

import asyncio

async def dohvati_podatke(): # definicija prve korutine
    lista1 = [{"id": 1, "name": "Ana"}, {"id":2, "name": "Marko" }] # listu proizvoljnih rječnika
    await asyncio.sleep(3) # nakon 3 sekunde
    return lista1

async def dohvati_proizvode():
    lista2 = [{"id": 1, "name": "mobitel"}, {"id":2, "name": "laptop" }] # listu proizvoljnih rječnika
    await asyncio.sleep(5) # nakon 5 sekundi
    return lista2

async def main(): # glavna korutina koja pokreće obje 
    lista1, lista2 = await asyncio.gather(dohvati_podatke(), dohvati_proizvode()) # naredba za porketanje obje okrutine: await asyncio.gather()
    print("Lista rječnika:" , lista1) # ispis liste1
    print("Lista proizvoda:", lista2) # ispis liste2
    
asyncio.run(main()) # naredba za pokretanje korutine asyncio.run()


