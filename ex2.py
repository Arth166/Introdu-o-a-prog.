#Faça um algoritmo em Python mostre na tela os 20 primeiros números da sequência (1 / 1), (-1 / 2), (1 / 3), (-1 / 4), ...
i = 1
j = 1
while j != 21:
    if(j%2 == 0):
        i = -1
        u = f"{i} / {j}"
        j+=1
    else:
        i=1
        u = f"{i} / {j}"
        j+=1
    print(f"({u})", end=" ")
