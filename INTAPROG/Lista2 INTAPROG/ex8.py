#Elabore um programa que leia três valores, encontre o maior dos três valores e o escreva com a mensagem: "É o maior”.
try:
    n1 = int(input("digite um intero: "))
    n2 = int(input("digite outro numero inteiro: "))
    n3 = int(input("digite mais um numero inteiro: "))
    if n1 >= n2 and n1 >= n3:
        print(f"{n1} é o maior.")
    elif n1 == n2 and n1 == n3:
        print(f"Os tres valores são iguais e são {n1}.")
    elif n2>=n1 and n2>=n3:
        print(f"{n2} é o maior.")
    else:
        print(f"{n3} é o maior.")
except ValueError as ERRO:
    print(f"Deu erro: {ERRO}")