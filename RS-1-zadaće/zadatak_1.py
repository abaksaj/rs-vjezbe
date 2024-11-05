br1 = float(input("Unesite prvi broj: "))
br2 = float(input("Unesite drugi broj: "))
operator = input("Unesite operator (+, -, *, /): ")

if operator == '+':
    rez = br1 + br2
    print(f"Rezultat operacije {br1} + {br2} je {rez}")
elif operator == '-':
    rez = br1 - br2
    print(f"Rezultat operacije {br1} - {br2} je {rez}")
elif operator == '*':
    rez = br1 * br2
    print(f"Rezultat operacije {br1} * {br2} je {rez}")
elif operator == '/':
    if br2 == 0:
        print("Dijeljenje s nulom nije dozvoljeno!")
    else:
        rez = br1 / br2
        print(f"Rezultat operacije {br1} / {br2} je {rez}")
else:
    print("Nepodržani operator")