'''Escrever um algoritmo que gera e escreve os cinco primeiros números perfeitos. Um número
perfeito é aquele que é igual à soma dos seus divisores.'''
n = 1
enc = 0
while enc < 5:
    s = 0
    div = 1
    while div <= n/2:
        if n%div == 0:
            s = s + div
        div += 1
    if s == n:
        print(n)
        enc += 1
    n += 1
