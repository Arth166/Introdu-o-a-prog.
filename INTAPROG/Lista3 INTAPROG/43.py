'''Escreva um algoritmo que calcula e escreve o produto dos números primos entre 92 e 1478.'''
n = 92
p = 1
while n < 1478:
    primo = True
    div = 2
    while div <= n/2:
        if n%div == 0:
            primo = False
            break
        div += 1
    if primo:
        p = p*n
    n+=1
print(p)