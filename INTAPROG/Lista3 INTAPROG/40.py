'''Foi realizada uma pesquisa de algumas características físicas da população de certa região,
a qual coletou os seguintes dados referentes a cada habitante para serem analisados: 
Sexo (masculino ou feminino)  
• Cor dos olhos (azul, verde ou castanho)  
• Cor dos cabelos (louro, castanho ou preto)  
• Idade. 
Faça um programa que determine e informe:

a. A maior idade dos habitantes;  
b. A quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive,
e que tenham olhos verdes e cabelos louros.
O final do conjunto de habitantes é reconhecido pelo valor -1, informado como idade. '''
sex = input('')
corol = input('')
corca = input('')
idade = int(input(''))
ma = idade
qnt = 0
while idade > -1:
    if idade > ma:
        ma = idade
    if sex == 'F' and idade >= 18 and idade < 36 and corol == 'verde' and corca == 'louro':
        qnt += 1
    sex = input('')
    corol = input('')
    corca = input('')
    idade = int(input(''))
if ma < -1:
    print('idade maior não informado.')
else:
    print(ma)
    print(qnt)