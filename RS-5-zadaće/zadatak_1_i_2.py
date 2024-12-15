import aiohttp
import asyncio
import json
from aiohttp import web

# zadatak 1 i zadatak 2

# rječnik proizvoda
proizvodi = [
{"naziv": "fritule", "cijena": 10.99, "količina": 100},
{"naziv": "brašno", "cijena": 5.49, "količina": 200},
{"naziv": "papir", "cijena": 20.00, "količina": 50},
]
# handler funkcija --> obrađuje zahtjeve i vraća odgovor klijentu
async def get_proizvodi(request): # request parametar sadrži info o zahtjevu
    
    return web.json_response(proizvodi) # hander funkcija vraća odgovor klijentu koji je ovdje JSON(string)

async def post_proizvodi(request):
    novi_proizvod = await request.json()
    print(novi_proizvod)
    proizvodi.append(novi_proizvod)
    return web.json_response(proizvodi)
    

# poziv aplikacije i ruta
app = web.Application()
app.router.add_get('/proizvodi', get_proizvodi)
app.router.add_post('/proizvodi', get_proizvodi)

# pokretanje poslužitelja
if __name__ == '__main__':
    web.run_app(app, port=8080)
