# korištenje for petlje
broj = int(input("Unesite broj za računanje faktorijela: "))
faktorijel = 1
for i in range(1, broj + 1):
    faktorijel *= i
print(f"Faktorijel od {broj} koristeći for petlju je: {faktorijel}")

#korištenje while petlje
broj= int(input("Enter a number to calculate its factorial: "))
faktorijel = 1
i = 1
while i <= broj:
    faktorijel *= i
    i += 1
print(f"Faktorijel od {broj} koristeći while petlju je: {faktorijel}")
