def broj_rijeci(text):
    rijeci = text.split()  
    rijeci_brojac = {}  
    
    for rijec in rijeci:
        rijec = rijec.lower()  
        if rijec in rijeci_brojac:
            rijeci_brojac[rijec] += 1  
        else:
            rijeci_brojac[rijec] = 1  
    
    return rijeci_brojac

# Primjer
text = "Python je popularan. Python je jednostavan za naučiti i koristiti."
print(rijeci_brojac(text))

