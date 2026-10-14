'''Escreva um programa que leia repetidamente um número inteiro V e um algarismo D, remova todas as ocorrências de D em V e imprima o inteiro resultante, mantendo a ordem dos demais algarismos.

O sinal negativo deve ser preservado quando o resultado for diferente de zero. Se todos os algarismos forem removidos, o resultado será 0. Zeros que ficarem à esquerda não devem aparecer na saída.

Exemplos: remover 0 de 102030 produz 123; remover 5 de -45554 produz -44; remover 1 de 1002 produz 2; remover 7 de 777 produz 0.

Regras obrigatórias:
- Utilize while para percorrer os algarismos e para controlar a leitura até a sentinela.
- Manipule os algarismos exclusivamente com operações aritméticas, como divisão inteira, resto, soma e multiplicação.
- É proibido converter os números em strings para manipular seus algarismos. O uso normal de input() e print() é permitido.
- É proibido utilizar listas, tuplas, conjuntos ou dicionários para armazenar os algarismos.

Entrada:
Um inteiro V por linha, com -1000000000 <= V <= 1000000000.
Se V for diferente de -1, a linha seguinte contém D, com 0 <= D <= 9.
O valor -1, lido no lugar de V, encerra o programa. Nesse caso, não existe uma linha com D e a sentinela não deve ser processada.

Saída:
Para cada par V e D, imprima o inteiro resultante em uma linha.
Ao ler a sentinela, imprima exatamente:
Programa encerrado!

Todas as entradas respeitam os limites informados; não é necessário validar a entrada. Não imprima mensagens além das especificadas.'''

v = int(input(''))
while v!=-1:
    negativo = False
    if v<0:
        v = -v
        negativo = True
    div = 1
    while v//div >= 10:
        div = div*10
    d = int(input(''))
    re = 0
    while div > 0:
        u = v//div
        if u != d:
            re = re *10 + u
        v = v%div
        div = div//10
    if negativo:
        print(-re)
    else:
        print(re)
    v = int(input(''))
print('Programa encerrado!')