for i in range(1, 2):
    print(i)
#Ova petlja će ispisati samo 1 jer range(1, 2) generira brojeve počevši od 1 do, ali ne uključujući, 2. Dakle, samo 1 je u ovom rasponu.

for i in range(1, 10, 2):
    print(i)
#Ova petlja ispisuje 1, 3, 5, 7, 9 jer raspon(1, 10, 2) počinje od 1 i ide do, ali ne uključujući, 10, povećavajući se za 2 svaki put.

for i in range(10, 1, -1):
    print(i)
#Ova petlja ispisuje 10, 9, 8, ..., 2 jer raspon (10, 1, -1) počinje od 10 i ide dolje do 2, smanjujući se za 1 svaki put. 
#Petlja isključuje 1 jer krajnja vrijednost u rasponu nije uključiva.