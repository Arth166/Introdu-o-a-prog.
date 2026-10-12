#Faça um programa que dados três números os imprima em ordem crescente.
try:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro númeo: "))
    n3 = int(input("Mais um vai: "))
    if n1 <= n2 and n2 <= n3:
        print(f"{n1}, {n2}, {n3}")
    elif n1 >= n2 and n2 >= n3:
        print(f"{n3}, {n2}, {n1}")
    elif n2 >= n1 and n1 >= n3:
        print(f"{n3, n1, n2}")
    elif n2>=n3 and n3>=n1:
        print(n1, n3, n2)
    elif n1>=n3 and n3>=n2:
        print(n2, n3, n1)
    else: 
        print(n2, n1, n3) 
except ValueError as ERRO:
    print(f"Deu erro: {ERRO}")