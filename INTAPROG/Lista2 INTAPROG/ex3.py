#Construa um programa que leia dois valores numéricos inteiros e efetue a adição; caso o resultado seja maior que 10, apresentá-lo.
try:
    n1 = int(input("Digite o primeiro número inteiro: "))
    n2 = int(input("Digite o segundo número inteiro: "))
    soma = n1 + n2
    if soma <= 10:
        print("A soma não é maior que dez.")
    else:
        print(f"A soma é {soma}")
except ValueError as ERRO:
    print(f"Deu erro: {ERRO}")