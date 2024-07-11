'''Crie uma função que receba uma lista de tuplas, cada uma contendo o
nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das
pessoas em ordem alfabética.'''

def ordenar_por_nome(pessoas):
    return sorted(pessoas, key=lambda pessoa: pessoa[0])  # Ordena pelo primeiro elemento (nome)

#Exemplo de uso:
pessoas = [("Jujuba", 2), ("Paçoca", 4), ("Tom", 5), ("Salém", 1)]
pessoas_ordenadas = ordenar_por_nome(pessoas)
print(pessoas_ordenadas)
