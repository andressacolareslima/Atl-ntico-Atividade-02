'''Escreva uma função que receba uma lista de números e retorne outra lista
com os números primos presentes.'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_prime(numeros):
    return [x for x in numeros if is_prime(x)]

#Exemplo de uso: 
numeros = [2, 1, 4, 5, 3, 9, 7, 12]
prime_numbers = get_prime(numeros)

print(prime_numbers) 
