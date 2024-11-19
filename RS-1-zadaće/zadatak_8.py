def filter_even_numbers(input_list):
    even_lista = []  # prazna lista za brojeve
    
    for num in input_list:
        if num % 2 == 0:  # provjera da li je broj paran
            even_lista.append(num)  
    return even_lista

# Primjer:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_even_numbers(lista))  #  [2, 4, 6, 8, 10]