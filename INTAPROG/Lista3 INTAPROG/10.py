'''Faça um programa que leia o nome de um aluno, a quantidade de provas realizadas por ele e suas
respectivas notas. O algoritmo deve apresentar ao final o nome e a média das notas obtidas do
aluno.'''

nome = input('nome: ')
qnt = int(input('provas realizadas: '))
s = 0
q = qnt
if qnt < 0:
    print(f'Vaza Caralho.')
else:
    while qnt != 0:
        nota = int(input('notas: '))
        s = s + nota
        qnt -= 1
    if qnt == 0:
        print(f'Nenhuma prova foi efetuada.')
    else:
        print(f'Nome: {nome}\nMédia: {s/q: .2f}.')