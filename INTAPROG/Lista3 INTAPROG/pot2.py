# Faça um algoritmo em Python mostre na tela as 20 primeiras potências de 2 (2, 4, 8, ...)
try:
    print("==============================================")
    print("     Responda apenas com 1(sim) ou 0(não)     ")
    a = int(input("Almeja ver todas as potências de 2 até 20? "))
    print("==============================================")
    if (a == 1):
        i = 2
        j = 0
        while (j != 21):
            u = i**j
            print(f"{u}", end=" ")
            j=j+1
    elif (a == 0):
        print("mec cria.")
    else:
        print("zero ou um sua mula burra.")
except Exception as ERRO:
    print(f"Deu erro: {ERRO}")


 