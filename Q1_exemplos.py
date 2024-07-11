'''Escreva uma função que receba uma lista de números e retorne outra lista
com os números ímpares.'''

def get_odd(numbers):
    return (i for i in numbers if i % 2 !=0 )

#Exemplo de uso:
numbers = [2,4,6,8,10,1,3,7,12,51]
impares = get_odd(numbers)
print (list(impares))