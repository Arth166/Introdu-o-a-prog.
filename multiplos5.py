try:
    n1 = int(input("Escolha um numero não negativo: "))
    n2 = int(input("Escolha outro numero não negativo: "))
    i = 5
    if n1 < n2:
        if i > n1 or i < n1:
            print("Não há múltiplos de 5 dentro desse intervalo.")
        else:
            while i < n2 and i > n1:
                print(i)
                i += 5
    elif n1 == n2 and n1 % 5 == 0:
        print(n1)
    else:
        if i > n1 or i < n1:
            print("Não há múltiplos de 5 dentro desse intervalo.")
        else: 
            while i < n1 and i > n2:
                print(i)
                i += 5
except Exception as ERRO:
    print(f"Seu BOXXXXTA: {ERRO}")