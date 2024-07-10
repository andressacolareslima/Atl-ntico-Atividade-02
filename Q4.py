'''Dada uma lista de números inteiros, escreva uma função para encontrar o
segundo maior valor na lista.'''

def segundo_maior(numeros):

    if len(numeros) < 2:
        return None

    remover_repeticao = list(set(numeros))
    remover_repeticao.sort(reverse=True)
    
    return remover_repeticao[1]

numeros_input = input("Separados por espaço, digite uma lista de números: ")
numeros_i = [int(i) for i in numeros_input.split()]
segundo_maior1 = segundo_maior(numeros_i)

if segundo_maior1 is not None:
    print (f"O segundo maior número dessa lista é: {segundo_maior1}")
else:
    print(f"A lista precisa ter pelo menos dois números diferentes. Tente novamente. ")