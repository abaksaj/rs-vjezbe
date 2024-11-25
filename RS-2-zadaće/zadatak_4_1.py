'''1. Definirajte klasu Automobil s atributima marka , model , godina_proizvodnje i kilometraža .
Dodajte metodu ispis koja će ispisivati sve atribute automobila.
Stvorite objekt klase Automobil s proizvoljnim vrijednostima atributa i pozovite metodu ispis .
Dodajte novu metodu starost koja će ispisivati koliko je automobil star u godinama, trenutnu
godine dohvatite pomoću datetime modula.'''

# Klasa je pravilo koje generira objekte i metode nad podacima
# Atributi se koriste za pohranjivanje podataka dok se metode koriste za definiranje ponašanja

from datetime import datetime  # modul za datum i vrijeme za računanje starosti automobila

class Automobil:  # Definirajte klasu Automobil
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):  # _init_ postavlja atribute kada se objekt kreira
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def print_atributi(self):  # metoda ispis
        return f"Marka: {self.marka}, Model: {self.model}, Godina_proizvodnje: {self.godina_proizvodnje}, Kilometraza: {self.kilometraza} km"
    
    def starost(self):  # Dodajte novu metodu starost
        godina = datetime.now().year  # dohvaćanje trenutne godine
        return godina - self.godina_proizvodnje

# Stvorite objekt klase Automobil s proizvoljnim vrijednostima atributa
automobil = Automobil("Toyota", "Corolla", 2015, 75000)

print(automobil.print_atributi())  # pozovite metodu ispis

# ispis metode starost
print(f"Starost: {automobil.starost()} godina")


    

    




    

