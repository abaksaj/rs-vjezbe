'''4. Definirajte klasu Krug s atributom r . Dodajte metode opseg i povrsina koje će računati opseg i
površinu kruga.
Stvorite objekt klase Krug s proizvoljnim radijusom i ispišite opseg i površinu kruga.'''

import math # matematičke funkcije

class Krug: # klasa Krug
    def __init__(self, r): # atribut r
        self.r = r

    def opseg(self): # metoda opseg
        return 2 * math.pi * self.r

    def povrsina(self): # metoda povrsina
        return math.pi * self.r ** 2

# Stvorite objekt klase Krug
krug = Krug(5) # proizvoljni radijus

# ispišite opseg i površinu kruga
print(f"Radius: {krug.r}")
print(f"Opseg: {krug.opseg():.2f}")
print(f"Površina: {krug.povrsina():.2f}")

