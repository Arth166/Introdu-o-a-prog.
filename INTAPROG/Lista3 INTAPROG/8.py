'''Faça um programa que imprima a média n de números (n é um valor lido do teclado) excluindo
o menor e o maior deles. Seu programa deve tratar casos em que n<3 exibindo uma mensagem
de erro.'''

n = int(input(''))
v = int(input(''))
if n < 3:
    print('Erro: Número deve ser maior que 3.')
else:
    s = v
    ma = v
    me = v
    i = 1
    while i < n:
        v = int(input(''))
        if v > ma:
            ma = v
        elif v < me:
            me = v 
        s = s + v
        i += 1
    s = s - (ma + me)
    print(s/(i - 2))
