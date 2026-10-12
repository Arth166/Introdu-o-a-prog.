'''Nesta questão, dois números são chamados de primos gêmeos quando ambos são primos e a diferença entre o maior e o menor é exatamente 2.

Um número primo é um inteiro maior que 1 que possui exatamente dois divisores positivos: 1 e ele próprio.

Leia um inteiro L e encontre todos os pares (p, p + 2) em que ambos os números são primos e estão no intervalo de 2 até L, inclusive. Imprima os pares em ordem crescente de p. Cada par deve aparecer apenas uma vez, mas um número pode participar de mais de um par.

Por exemplo, para L = 7, os pares são 3 5 e 5 7. O par 2 3 não deve ser impresso, pois a diferença é 1.'''

n = int(input(''))
m = 2
k = 2
if n <= 1:
    primo = False
imprimiu = False
while m <= n:
    divisor = 2
    primo = True
    while divisor < m:
        u = m%divisor
        if u == 0:
            primo = False
        divisor += 1
    if primo and m - k == 2:
        print(f'{k} {m}')   
        imprimiu = True
    if primo:
        k = m
    m += 1
if not imprimiu:
    print('Nenhum par encontrado!')
