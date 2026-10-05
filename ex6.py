#Escreva um programa que verifique se um valor de entrada x pertence ao intervalo ]-10, 30]
try:
    n1 = int(input("Digite um numero inteiro: "))
    if n1 > -10 and n1 <= 30:
        print("O número está dentro do intervalo.")
    else:
        print("O numero não está no intervalo.")
except ValueError as ERRO:
    print(f"Deu erro: {ERRO}")