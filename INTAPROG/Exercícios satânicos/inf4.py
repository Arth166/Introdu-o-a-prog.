"""Três sensores registram valores inteiros em cada medição. Para reduzir o efeito de valores extremos, o sistema deve utilizar a mediana 
das três leituras. A mediana de três valores é o valor que ocupa a posição central quando os valores são colocados em ordem crescente. 
Valores repetidos são permitidos.Exemplos: a mediana de 9, 2 e 5 é 5; a mediana de 4, 4 e 10 é 4; a mediana de -3, 0 e -1 é -1."""

n = int(input(''))
i = 1
while i <= n:
    a = int(input(''))
    b = int(input(''))
    c = int(input(''))
    if (a >= b and a <= c) or (a >= c and a <= b):
        print(a)
    elif (b >= a and b <= c) or (b >= c and b <= a):
        print(b)
    else:
        print(c) 
    i += 1