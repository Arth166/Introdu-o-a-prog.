#Faça um programa para ler dois valores reais e verificar se são iguais, imprimindo como respostauma mensagem de confirmação.
try:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    if n1 == n2:
        print(f"Os números {n1} e {n2} são iguais.")
    else:
        print(f"Os números {n1} e {n2} são diferentes.")
except ValueError as ERRO:
    print(f"Deu erro: {ERRO}") 