#Faça um programa que leia um número inteiro maior que zero e informe se tal número é par ouímpar.
try: 
    n = int(input("Digite um número inteiro maior que zero: "))
    if n % 2 == 0:
        print(f"O número {n} é par.")
    elif n < 0:
        print("O número digitado não é maior que zero.")
    else:
        print(f"O número {n} é ímpar.")
except ValueError as ERRO:
    print(f"Deu erro: {ERRO}")