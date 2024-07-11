# Criaremos um programa para substituir números por palavras em uma lista
# 1. Crie uma lista com 15 números
# 2. Crie um for loop para percorrer todos os elementos da lista
# 3. Crie uma estrutura condicional para verificar cada número da lista:
# 3.1 Caso o número seja divisível por 3, substitua-o por "Fizz"
# 3.2 Caso o número seja divisível por 5, substitua-o por "Buzz"
# 3.3 Caso o número seja divisível por 3 e 5, substitua-o por "FizzBuzz"


numeros = list(range(1, 16))
for i in range(len(numeros)):
    if numeros[i] % 3 == 0 and numeros[i] % 5 == 0:
        numeros[i] = "FizzBuzz"
    elif numeros[i] % 3 == 0:
        numeros[i] = "Fizz"
    elif numeros[i] % 5 == 0:
        numeros[i] = "Buzz"
print("Lista após substituições:")
print(numeros)
