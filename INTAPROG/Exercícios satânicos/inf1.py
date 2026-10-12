'''Escreva um programa que leia repetidamente um número inteiro V e um algarismo D, remova todas as ocorrências de D em V e imprima o inteiro resultante, mantendo a ordem dos demais algarismos.

O sinal negativo deve ser preservado quando o resultado for diferente de zero. Se todos os algarismos forem removidos, o resultado será 0. Zeros que ficarem à esquerda não devem aparecer na saída.

Exemplos: remover 0 de 102030 produz 123; remover 5 de -45554 produz -44; remover 1 de 1002 produz 2; remover 7 de 777 produz 0.

Regras obrigatórias:
- Utilize while para percorrer os algarismos e para controlar a leitura até a sentinela.
- Manipule os algarismos exclusivamente com operações aritméticas, como divisão inteira, resto, soma e multiplicação.
- É proibido converter os números em strings para manipular seus algarismos. O uso normal de input() e print() é permitido.
- É proibido utilizar listas, tuplas, conjuntos ou dicionários para armazenar os algarismos.'''


v = int(input(''))
if v <= -1000000000 or v >1000000000:
    print('número inválido.')
else:
    while v != -1:
        d = int(input(''))
        if d < 0 or d > 9:
            print('número inválido')
        else: 
            negativo = False
            if v < 0:
                negativo = True
                v = -v
            div = 1
            while v // div >= 10:
                div = div * 10
            comecou = False
            imprimiu = False
            while div > 0:
                u = v // div
                if d != u and (u != 0 or comecou):
                        if not comecou and negativo:
                            print('-', end='')
                        print(u, end='')
                        comecou = True
                        imprimiu = True
                v = v % div
                div = div // 10
            if imprimiu==False:
                print(0)
            v = int(input('\n'))
    print('Programa encerrado!')
