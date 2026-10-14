'''Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados de idade, sexo (‘M’ ou ‘F’) e salário. 
Faça um algoritmo que informe:
a. A média de salário do grupo;  
b. Maior e menor idade do grupo;  
c. Quantidade de mulheres com salário até R$1000,00. '''

idade = int(input(''))
sexo = input('')
sal = int(input(''))
s = 0
q = 1
qnt = 0
ma = idade
me = idade
while idade > -1:
    s = s + sal
    if idade > ma:
        ma = idade
    elif idade < me:
        me = idade
    if sexo == 'F' and sal <= 1000:
        qnt +=1
    idade = int(input(''))
    if idade <= -1:
        break
    sexo = input('')
    sal = int(input(''))
    q += 1
print(s/q)
print(ma, me)
print(qnt)