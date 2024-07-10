'''Crie uma função que receba uma lista de tuplas, cada uma contendo o
nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das
pessoas em ordem alfabética.'''

def order_pessoas(lista_nomes):
    return sorted(lista_nomes, key=lambda x:x[0])

qndt_registrar = int (input("Quantas pessoas você quer registrar? "))

pessoas_registradas = []

for i in range(qndt_registrar):
    nome = input("Nome da pessoa: ")
    idade = int (input("Idade da pessoa: "))
    pessoas_registradas.append((nome, idade))

tupla_ordenada = order_pessoas(pessoas_registradas)
for x in tupla_ordenada:
    print (f'[Nome: {x[0]} Idade: {x[1]}]', end='', sep='-')