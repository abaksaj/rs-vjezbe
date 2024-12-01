'''2. Definirajte dvije korutine, od kojih će jedna služiti za dohvaćanje činjenica o mačkama koristeći
get_cat_fact korutinu koja šalje GET zahtjev na URL: https://catfact.ninja/fact . Izradite 20
Task objekata za dohvaćanje činjenica o mačkama te ih pozovite unutar main korutine i rezultate
pohranite odjednom koristeći asyncio.gather funkciju. Druga korutina filter_cat_facts ne šalje
HTTP zahtjeve, već mora primiti gotovu listu činjenica o mačkama i vratiti novu listu koja sadrži samo
one činjenice koje sadrže riječ "cat" ili "cats" (neovisno o velikim/malim slovima).'''

import asyncio
import aiohttp

async def get_cat_fact(session):  # Korutina za dohvaćanje činjenica o mačkama
    response = await session.get("https://catfact.ninja/fact")
    data = await response.json()
    return data["fact"]

def filter_cat_facts(facts):  # korutina
    return [fact for fact in facts if "cat" in fact.lower() or "cats" in fact.lower()]

async def main():  # Glavna korutina
    async with aiohttp.ClientSession() as session:  
        # Kreiranje Task objekata za 20 činjenica o mačkama
        tasks = [get_cat_fact(session) for _ in range(20)]
        cat_facts = await asyncio.gather(*tasks)

        # Filtriranje činjenica
        filtered_facts = filter_cat_facts(cat_facts)
        print(f"Filtrirane činjenice o mačkama:\n{filtered_facts}")

# Pokretanje glavne korutine
asyncio.run(main())
