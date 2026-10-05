#Faça um programa que receba um número e mostre uma mensagem caso este número seja maior que 80, menor que 25 ou igual a 40.
try:
    nu = int(input("Digite um número: "))
    if nu > 80:
        print("O número é maior que 80.")
    elif nu < 25:
        print("O número é menor que 25.")
    elif nu == 40:
        print("O número é igual a 40.")
    else:
        print(" ")
except ValueError as ERRO:
    print(f"Deu erro: {ERRO}")