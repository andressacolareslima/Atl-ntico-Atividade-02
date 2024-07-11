''' Escreva uma função que receba duas listas e retorne outra lista com os
elementos que estão presentes em apenas uma das listas.'''

def unicos (lista1, lista2):
    return list (set(lista1).symmetric_difference(set(lista2)))

#Exemplo de uso:
lista1  = [1, 3, 6, 18, 9, 10]
lista2 = [2, 1, 4, 5, 11, 3, 6]

numeros_unicos = unicos(lista1, lista2)

print (numeros_unicos)