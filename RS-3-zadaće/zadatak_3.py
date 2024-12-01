'''3. Definirajte korutinu autentifikacija() koja će simulirati autentifikaciju korisnika na
poslužiteljskoj strani. Korutina kao ulazni parametar prima rječnik koji opisuje korisnika, a sastoji se
od ključeva korisnicko_ime , email i lozinka . Unutar korutine simulirajte provjeru korisničkog
imena na način da ćete provjeriti nalaze li se par korisnicko_ime i email u bazi korisnika. Ova
provjera traje 3 sekunde.'''

'''Ako se korisnik ne nalazi u bazi, vratite poruku "Korisnik {korisnik} nije pronađen."
Ako se korisnik nalazi u bazi, potrebno je pozvati vanjsku korutinu autorizacija() koja će simulirati
autorizaciju korisnika u trajanju od 2 sekunde. Funkcija kao ulazni parametar prima rječnik korisnika iz baze
i lozinku proslijeđenu iz korutine autentifikacija() . Autorizacija simulira dekripciju lozinke (samo
provjerite podudaranje stringova) i provjeru s lozinkom iz baze_lozinka. Ako su lozinke jednake, korutine
vraća poruku "Korisnik {korisnik}: Autorizacija uspješna." , a u suprotnom "Korisnik
{korisnik}: Autorizacija neuspješna." .

Korutinu autentifikacija() pozovite u main() 
funkciji s proizvoljnim korisnikom i lozinkom.
'''

import asyncio

baza_korisnika = [
{'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
{'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
{'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
{'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
{'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
{'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
{'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
{'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

import asyncio

# Baza korisnika (korisničko ime i email)
baza_korisnika = [
    {'korisnicko_ime': 'mirkol23', 'email': 'mirkol23egmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanicegmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaaggmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032egmail.com'}
]

# Baza lozinki (korisničko ime i lozinka)
baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

# Korutina za autorizaciju
async def autorizacija(korisnik, lozinka):

    await asyncio.sleep(2)  
    for zapis in baza_lozinka:
        if zapis['korisnicko_ime'] == korisnik['korisnicko_ime']:
            if zapis['lozinka'] == lozinka:
                return f"Korisnik {korisnik['korisnicko_ime']}: Autorizacija uspješna."
            else:
                return f"Korisnik {korisnik['korisnicko_ime']}: Autorizacija neuspješna."
    return f"Korisnik {korisnik['korisnicko_ime']}: Lozinka nije pronađena u bazi."

# Korutina za autentifikaciju
async def autentifikacija(korisnik):
    
    await asyncio.sleep(3)  
    for zapis in baza_korisnika:
        if zapis['korisnicko_ime'] == korisnik['korisnicko_ime'] and zapis['email'] == korisnik['email']:
            # Ako je korisnik pronađen, poziva se korutina za autorizaciju
            return await autorizacija(zapis, korisnik['lozinka'])
    return f"Korisnik {korisnik['korisnicko_ime']} nije pronađen."


async def main(): # definicija korutine main()

    test_korisnik = {
        'korisnicko_ime': 'ana_anic',
        'email': 'aanicegmail.com',
        'lozinka': 'super_teska_lozinka' # ispravna lozinka iz baze
    }
    
    rezultat = await autentifikacija(test_korisnik)
    print(rezultat)

    # Testiranje drugog korisnika
    test_korisnik_2 = {
        'korisnicko_ime': 'maja_0x',
        'email': 'majaaaaaggmail.com',
        'lozinka': 'kriva_lozinka'  # pogrešna lozinka koje nam u bazi
    }
    
    rezultat = await autentifikacija(test_korisnik_2)
    print(rezultat)

asyncio.run(main()) # pokreće glavnu korutinu main()
