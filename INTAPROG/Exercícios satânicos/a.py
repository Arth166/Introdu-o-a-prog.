
v = int(input(''))

while v != -1:
    div = 1
    negativo = False

    if v < 0:
        negativo = True
        v = -v

    while v // div >= 10:
        div = div * 10

    k = -1
    resultado = 0
    imprimiu = False

    while div > 0:
        u = v // div

        if u != k:
            resultado = resultado * 10 + u
            imprimiu = True

        k = u
        v = v % div
        div = div // 10

    if imprimiu:
        if negativo:
            resultado = -resultado
        print(resultado)
    else:
        print(0)

    v = int(input(''))

print('Programa encerrado!')