''' Escreva uma função que receba duas listas e retorne outra lista com os
elementos que estão presentes em apenas uma das listas.'''

def simetricos ():
    lista1 = input("Digite a primeira lista: ")
    lista2 = input("Agora, digite a segunda lista: ")

    lista1 = lista1.split()
    lista2 = lista2.split()

    frist_list = set(lista1)
    second_list = set(lista2)

    elements = (frist_list.symmetric_difference(second_list))
    return elements

diferent_element = simetricos()
if diferent_element:
    print (f'Os elementos presentes em apenas uma das listas são: {diferent_element}')
else:
    print("Essas listas não possuem elementos diferentes. Tente novamente. ")