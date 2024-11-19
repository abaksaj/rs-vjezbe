broj = 0
# Petlja svaki put povećava broj za 2 i ispisuje ga sve dok broj ne bude manji od 5.

broj = 0
while broj < 5:
    broj += 1
    print(broj)
    broj -= 1
#Ova petlja povećava broj za 1, ispisuje ga, zatim odmah smanjuje broj za 1.
#Petlja je beskonačna jer se broj uvijek vraća na 0.

broj = 10
while broj > 0:
    broj -= 1
    print(broj)
    if broj < 5:
        broj += 2
#Ova petlja smanjuje broj za 1 i ispisuje ga. Ako je broj manji od 5, dodaje 2 broju.
