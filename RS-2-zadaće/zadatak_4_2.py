'''2. Definirajte klasu Kalkulator s atributima a i b . Dodajte metode zbroj , oduzimanje , mnozenje ,
dijeljenje , potenciranje i korijen koje će izvršavati odgovarajuće operacije nad atributima a i
b .'''

class Kalkulator:
    def __init__(self, a, b):  # _init_ postavlja atribute kada se objekt kreira, atributi su a i b
        self.a = a
        self.b = b

    def zbroj(self):  # metoda zbroj
        return self.a + self.b

    def oduzimanje(self):  # metoda oduzimanje
        return self.a - self.b

    def mnozenje(self):  # metoda množenje
        return self.a * self.b

    def dijeljenje(self):  # metoda dijeljenje
        if self.b != 0:
            return self.a / self.b
        else:
            return "Dijeljenje sa 0 nije dozvoljeno!"

    def potenciranje(self):  # metoda potenciranje
        return self.a ** self.b

    def korijen(self):  # metoda korijen
        if self.b != 0:
            return self.a ** (1 / self.b)
        else:
            return "Korijen s nulom u nazivniku nije definiran!"


# Stvaranje objekta kalkulator
kalkulator = Kalkulator(18, 5)

# Pozivanje metoda
print("Zbroj:", kalkulator.zbroj())
print("Oduzimanje:", kalkulator.oduzimanje())
print("Množenje:", kalkulator.mnozenje())
print("Dijeljenje:", kalkulator.dijeljenje())
print("Potenciranje:", kalkulator.potenciranje())
print("Korijen:", kalkulator.korijen())




    