def check_password(password):
    # Provjerite je li duljina lozinke manja od 8 ili veća od 15
    if len(password) < 8 or len(password) > 15:
        print("Lozinka mora sadržavati između 8 i 15 znakova.")  
        return  
    
    #Provjerite ima li lozinka barem jedno veliko slovo i jednu znamenku
    if not any(char.isupper() for char in password) or not any(char.isdigit() for char in password):
        print("Lozinka mora sadržavati najmanje jedno veliko slovo i jedan broj.")  
        return  
    
    # Provjerite sadrži li lozinka riječ "lozinka" u bilo kojem slučaju 
    if "password" in password.lower():
        print("Lozinka ne smije sadržavati riječi 'password' ili 'PASSWORD'.")  
        return 
    
    # Ako su ispunjeni svi uvjeti, lozinka se smatra jakom
    print("Lozinka je jaka!")  

# Primjer
password = input("Unesite password: ")  
check_password(password)  