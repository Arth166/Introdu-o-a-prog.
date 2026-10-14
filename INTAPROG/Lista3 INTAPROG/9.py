'''Elabore um algoritmo que leia um valor x e logo após um número n que indicará a quantidade
de números a serem lidos após a leitura de n. Em seguida, leia n números (conforme o valor
informado anteriormente) e, ao final imprima se o elemento x aparece e sua posição, caso positivo.'''

x = int(input(''))
n = int(input(''))
i = 0
pos = 1
enc = 0
while i < n:
    v = int(input(''))
    if v == x:
        enc += 1
        if enc == 1:
            u = pos
    pos += 1
    i += 1
print(f'x aparece primeiro na posicao {u} e foi encontrado {enc} vez(es).') 