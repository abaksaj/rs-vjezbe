'''5. Definirajte korutinu secure_data koja će simulirati enkripciju osjetljivih podataka. Kako se u
praksi enkripcija radi na poslužiteljskoj strani, korutina će simulirati enkripciju podataka u trajanju od 3
sekunde. Korutina prima kao argument rječnik osjetljivih podataka koji se sastoji od ključeva prezime ,
broj_kartice i CVV . Definirajte listu s 3 rječnika osjetljivih podataka. Pohranite u listu zadaci kao u
prethodnom zadatku te pozovite zadatke koristeći asyncio.gather() . Korutina secure_data mora za
svaki rječnik vratiti novi rječnik u obliku: {'prezime': prezime , 'broj_kartice': 'enkriptirano',
'CVV': 'enkriptirano'} . Za fake enkripciju koristite funkciju hash(str) koja samo vraća hash
vrijednost ulaznog stringa.'''



import asyncio

async def secure_data(osjetljivi_podaci): # definicija korutine secure_data(osjetljivi_podaci):, argument su osjetljivi_podaci
    await asyncio.sleep(3)  # čekaj 3 sek
    return {
        'prezime': osjetljivi_podaci['prezime'],
        'broj_kartice': ''.join('*' for _ in osjetljivi_podaci['broj_kartice']),
        'CVV': ''.join('*' for _ in osjetljivi_podaci['CVV'])
    }

async def main():
    
    # Definirajte listu s 3 rječnika osjetljivih podataka.
    popis_osjetljivih_podataka = [
        {
            'prezime': 'Smith',
            'broj_kartice': '1234-5678-9012-3456',
            'CVV': '123'
        },
        {
            'prezime': 'Doe',
            'broj_kartice': '9876-5432-1098-7654',
            'CVV': '456'
        }
        
    ]

    zadaci = [secure_data(osjetljivi_podaci) for osjetljivi_podaci in popis_osjetljivih_podataka]

    # Paralelno izvršavanje svih zadataka za osiguravanje podataka
    print("Rezultati:")
    rezultati = await asyncio.gather(*zadaci) # način *zadaci kako se pozivaju sve koroutine sa .gather()

    # Ispis 
    for rezultat in rezultati:
        print(rezultat)

if __name__ == '__main__':
    # asyncio.run() pokreće glavnu funkciju
    asyncio.run(main())
