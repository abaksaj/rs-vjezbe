from aiohttp import web

async def get_punoljetni(request):
    korisnici = [{"ime": "Ana", "godine": 17},
                 {"ime": "Ivan", "godine": 22},
                 {"ime": "Marko", "godine": 19},
                 {"ime": "Petra", "godine": 16},
                 {"ime": "Lana", "godine": 21},
                 ]
    # logika za filtriranje korisnika koji su punoljetni
    punoljetni = [korisnik for korisnik in korisnici if korisnik['godine'] >=18 ]
    return web.json_response(punoljetni)

app = web.Application()
app.router.add_get('/punoljetni', get_punoljetni)

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8082)
    
    