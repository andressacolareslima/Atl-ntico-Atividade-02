'''Escreva uma função que receba uma lista de números e retorne outra lista
com os números primos presentes.'''

def prime_numbers():
    values = input("Digite uma lista de números, separados por espaço: ")
    numbers = [int(i) for i in values.split()]
    print(f'Os números selecionados foram: {numbers}')

    prime_numbers = []
    for num in numbers:
        if num > 1: 
            is_prime = True
            for i in range(2, int(num**0.5) + 1): 
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(num)

    return prime_numbers


all_primes = prime_numbers()
if all_primes:
    print(f"Os números primos dessa lista são: {all_primes}")
else:
    print("Não foram encontrados números primos. Tente novamente.")
