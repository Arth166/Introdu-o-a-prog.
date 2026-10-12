#Criar um programa que leia dois números e escreva qual deles elevado ao quadrado resulta no menor valor.
n1 = int(input("Digite um numero inteiro: "))
n2 = int(input("Digite outro numero inteiro: "))
if n1**2 > n2**2:
    print(f"{n2}² resulta no menor valor.")
elif n2**2 > n1**2:
    print(f"{n1}² representa o menor valor.")
else: 
    print("Ambos números ao quadrado possuem mesmo valor.")