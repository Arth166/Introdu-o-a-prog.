def add_not():
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    Med = media(n1, n2, n3)
    return Med
    
def media(x, y, z):
    return(x+y+z)/3

def impri(x, y, z):
    resul = f"Aluno {x} - Média: {y: .2f} **{z}**\n"
    return resul

def main():
    p = ""
    a = ''
    c = 1
    result = "**Resultados:**\n"
    while p != "N":
        estado = ""
        add = add_not()
        if add >= 7:
            estado = "Aprovado"
        elif add < 7 and add >= 5:
            estado = "Recuperação"
        else:
            estado = "Reprovado"
        a += impri(c, add, estado)
        p = input()
        c += 1
    print(result, end=(''))
    print(a, end=(''))

main()