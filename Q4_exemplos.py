'''Dada uma lista de números inteiros, escreva uma função para encontrar o
segundo maior valor na lista.'''

def encontrar_segundo_maior(numeros):

    if len(numeros) < 2:
        return None 

    maior = float('-inf')
    segundo_maior = float('-inf')

    for num in numeros:
        if num > maior:
            segundo_maior = maior
            maior = num
        elif num > segundo_maior:
            segundo_maior = num

    return segundo_maior

#Exemplos de uso:
#Lista com Números Distintos
numeros1 = [5, 12, 8, 3, 9]
segundo_maior_valor1 = encontrar_segundo_maior(numeros1)
print(segundo_maior_valor1)

# Lista com Números Repetidos
numeros2 = [10, 10, 5, 2]
segundo_maior_valor2 = encontrar_segundo_maior(numeros2)
print(segundo_maior_valor2) 

#Lista com um Único Elemento
numeros3 = [7]
segundo_maior_valor3 = encontrar_segundo_maior(numeros3)
print(segundo_maior_valor3)

# Lista Vazia
numeros4 = []
segundo_maior_valor4 = encontrar_segundo_maior(numeros4)
print(segundo_maior_valor4) 