'''5. Definirajte klasu Radnik s atributima ime , pozicija , placa . Dodajte metodu work koja će ispisivati
"Radim na poziciji {pozicija}".
Dodajte klasu Manager koja nasljeđuje klasu Radnik i definirajte joj atribut department . Dodajte
metodu work koja će ispisivati "Radim na poziciji {pozicija} u odjelu {department}".
U klasu Manager dodajte metodu give_raise koja prima parametre radnik i povecanje i
povećava plaću radnika ( Radnik ) za iznos povecanje .
Definirajte jednu instancu klase Radnik i jednu instancu klase Manager i pozovite metode work i
give_raise .'''

class Randik: # klasa Radnik
    def __init__(self, ime, pozicija, plaća): # s atributima ime , pozicija , placa
        self.ime = ime
        self.pozicija = pozicija
        self.plaća = plaća
    
    def work(self): # metoda work
        print(f"Radim na poziciji {self.pozicija}.") # ispisivati "Radim na poziciji {pozicija}

        

class Manager(Randik): # klasa Manager koja nasljeđuje klasu Radnik
    def __init__(self, ime, pozicija, plaća, department):
        super().__init__(ime, pozicija, plaća) #  nasljeđujemo atribute od nadklase
        self.department = department

    def work(self): # metoda work
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}.")

    def give_raise(self, radnik, povećanje): # metoda give_raise
        radnik.plaća += povećanje
        print(f"{radnik.ime} tvoja plaća je: {radnik.plaća}")

# Stvorite objekte radnik i manager
radnik1 = Randik("Ana", "Developer", 50000) # instancu klase Radnik i jednu instancu klase Manager
manager1 = Manager("Mario", "Team Lead", 70000, "Engineering")

# Poziv metoda
radnik1.work()
manager1.work()

# Manager daje povišicu radniku
manager1.give_raise(radnik1, 5000)