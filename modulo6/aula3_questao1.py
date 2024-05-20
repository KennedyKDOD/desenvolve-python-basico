
numeros = []
while len(numeros) < 4:
    num = int(input("Digite um número inteiro (digite 'q' para parar): "))
    numeros.append(num)
    
# Solicita números adicionais até que o usuário digite 'q'
while True:
    entrada = input("Digite um número inteiro (ou 'q' para parar): ")
    if entrada.lower() == 'q':
        break
    try:
        num = int(entrada)
        numeros.append(num)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")


print("Lista original:", numeros)

print("Os 3 primeiros elementos:", numeros[:3])

print("Os 2 últimos elementos:", numeros[-2:])

print("Lista invertida:", numeros[::-1])

print("Elementos de índice par:", numeros[::2])

print("Elementos de índice ímpar:", numeros[1::2])
