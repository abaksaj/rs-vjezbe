'''1. Definirajte korutinu fetch_users koja će slati GET zahtjev na JSONPlaceholder API na URL-u:
https://jsonplaceholder.typicode.com/users . Morate simulirate slanje 5 zahtjeva konkurentno
unutar main korutine. Unutar main korutine izmjerite vrijeme izvođenja programa, a rezultate
pohranite u listu odjedanput koristeći asyncio.gather funkciju. Nakon toga koristeći map funkcije ili
list comprehension izdvojite u zasebne 3 liste: samo imena korisnika, samo email adrese korisnika i
samo username korisnika. Na kraju main korutine ispišite sve 3 liste i vrijeme izvođenja programa.'''

import time
import asyncio
import aiohttp


async def fetch_users(): # defincija korutine fetch_users():  
    url = "https://jsonplaceholder.typicode.com/users" 
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main(): # definicija main() korutine
    start_time = time.time() # mjeri vrijeme slanja zahtjeva

    zahtjevi = [fetch_users() for _ in range(5)] # simulacija slanja 5 zahtjeva konkurentno
    rezultat_zahtjevi = await asyncio.gather(*zahtjevi) # pohrana rezultata u listu uz pomoć asyncio.gather funkcije

    # ekstrakcija informacija uz list comoprehension
    users = rezultat_zahtjevi[0]  # ovo su podaci iz jasona
    names = [user["name"] for user in users]
    emails = [user["email"] for user in users]
    usernames = [user["username"] for user in users]
    
    # ekstrakcija uz pomoć map funkcije
    #users = rezultat_zahtjevi[0]  # ovo su podaci iz jasona
    #names = list(map(lambda user: user["name"], users))
    #emails = list(map(lambda user: user["email"], users))
    #usernames = list(map(lambda user: user["username"], users))

    
    # ispis rezultata
    print(f"Names: {names}")
    print(f"Emails: {emails}")
    print(f"Usernames: {usernames}")

    # ispis rezultata
    print(f"Vrijeme ispisa: {time.time() - start_time} seknude")

asyncio.run(main())