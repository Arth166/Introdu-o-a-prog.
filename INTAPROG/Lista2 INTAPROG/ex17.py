"""Uma empresa concederá um aumento de salário aos seus funcionários, variável de acordo com o
cargo, conforme a tabela abaixo. Faça um programa que leia o salário e um código relativo ao
cargo de um funcionário e calcule o novo salário. Seu programa deve informar o cargo do
funcionário, salário antigo, o novo salário e a diferença.

Código Cargo Percentual (%)
101 Gerente 0
102 Analista 0,5%
103 Programador 1,5%
104 Designer 3%

Obs.:Se o cargo do funcionário não estiver na tabela, ele deverá, então, receber 40% de aumento
e seu programa deve exibir a mensagem “Cargo desconhecido”."""

Sal = int(input('Digite o seu salário atual: '))
Cod = int(input('Digite o código do salário: '))

if Cod == 101:
    print(f'Cargo: Gerente\nSalário antigo: {Sal}\nSalário novo: {Sal}\nDiferença: 0')
elif Cod == 102:
    Saln = Sal *1.005
    Dif = Saln - Sal
    print(f'Cargo: Analista\nSalário antigo: {Sal}\nSalário novo: {Saln: .2f}\nDiferença: {Dif: .2f}')
elif Cod == 103:
    Saln = Sal *1.015
    Dif = Saln - Sal
    print(f'Cargo: Programador\nSalário antigo: {Sal}\nSalário novo: {Saln: .2f}\nDiferença: {Dif: .2f}')
elif Cod == 104:
    Saln = Sal *1.03
    Dif = Saln - Sal
    print(f'Cargo: Designer\nSalário antigo: {Sal}\nSalário novo: {Saln: .2f}\nDiferença: {Dif: .2f}')
else: 
    Saln = Sal *1.4
    Dif = Saln - Sal
    print(f'Cargo desconhecido\nSalário antigo: {Sal}\nSalário novo: {Saln: .2f}\nDiferença: {Dif: .2f}')