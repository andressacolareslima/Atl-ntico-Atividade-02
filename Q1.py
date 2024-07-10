'''Escreva uma função que receba uma lista de números e retorne outra lista
com os números ímpares.'''

def odd ():
    valores = input("Digite uma lista de números, separadas por espaço: ")
    convert = [int(i) for i in valores.split()]
    print(f'Os números selecionados foram: {convert}')
    select_odd = [i for i in convert if i % 2 !=0]
    return select_odd
all_odd = odd()
if all_odd:
    print(f"Os números ímpares dessa lista são: {all_odd}")
else:
    print("Não foram encontrados números ímpares. Tente novamente.")