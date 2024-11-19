def remove_duplicates(input_list):
    lista_a = []  # prazna lista
    
    for item in input_list:
        if item not in lista_a = []  # prazna lista

            lista_a.append(item)  
    
    return lista_a

# Primjer
lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(remove_duplicates(lista))  #  [1, 2, 3, 4, 5]