# Faça um algoritmo em Python mostre na tela as 20 primeiras potências de 2 (2, 4, 8, ...)
i = 2
j = 1
while (j != 21):
    u = i**j
    print(f"{u}", end=" ")
    j=j+1
