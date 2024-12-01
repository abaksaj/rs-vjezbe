'''3. Definirajte korutinu get_dog_fact koja dohvaća činjenice o psima sa DOG API.
Korutina get_dog_fact neka dohvaća činjenicu o psima na URL-u: https://dogapi.dog/api/v2/facts .
Nakon toga, definirajte korutinu get_cat_fact koja dohvaća činjenicu o mačkama slanjem zahtjeva na
URL: https://catfact.ninja/fact .
Istovremeno pohranite rezultate izvršavanja ovih Taskova koristeći asyncio.gather(*dog_facts_tasks,
*cat_facts_tasks) funkciju u listu dog_cat_facts , a zatim ih koristeći list slicing odvojite u dvije liste
obzirom da znate da je prvih 5 činjenica o psima, a drugih 5 o mačkama.
Na kraju, definirajte i treću korutinu mix_facts koja prima liste dog_facts i cat_facts i vraća novu
listu koja za vrijednost indeksa i sadrži činjenicu o psima ako je duljina činjenice o psima veća od duljine
činjenice o mačkama na istom indeksu, inače vraća činjenicu o mački. Na kraju ispišite rezultate filtriranog
niza činjenica. Liste možete paralelno iterirati koristeći zip funkciju, npr. for dog_fact, cat_fact in
zip(dog_facts, cat_facts).'''

import aiohttp
import asyncio

async def get_dog_fact(session):  # Korutina get_dog_fact sa deljenom sesijom
        response = await session.get("https://dogapi.dog/api/v2/facts")
        data = await response.json()
        return data["data"][0]["attributes"]["body"]

async def get_cat_fact(session):  # Korutina get_cat_fact sa deljenom sesijom
        response = await session.get("https://catfact.ninja/fact")
        data = await response.json()
        return data["fact"]

async def mix_facts(dog_facts, cat_facts):  # Mix dog and cat facts
    return [
        dog_fact if len(dog_fact) > len(cat_fact) else cat_fact
        for dog_fact, cat_fact in zip(dog_facts, cat_facts)
    ]

async def main():  # Glavna korutina
    async with aiohttp.ClientSession() as session: 
        
        dog_facts_tasks = [get_dog_fact(session) for _ in range(5)]
        cat_facts_tasks = [get_cat_fact(session) for _ in range(5)]
        
        # dohvaćanje 
        dog_cat_facts = await asyncio.gather(*dog_facts_tasks, *cat_facts_tasks)
        dog_facts = dog_cat_facts[:5]  # Činjenice o psima
        cat_facts = dog_cat_facts[5:]  # Činjenice o mačkama
        
    
        mixed_facts = await mix_facts(dog_facts, cat_facts)
        print(f"Mixed Facts:\n{mixed_facts}")

# Pokretanje glavne korutine
asyncio.run(main())
