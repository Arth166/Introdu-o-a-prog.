def implista(n):
    i = 0
    while i < len(n):
        print(n[i])
        i += 1

#programa que le nota de uma turma e as add em uma lista.só para de ler valores quando valor neg
#remove todo num menor q 6.5
def main():
    p = float(input())
    n = []
    while p >= 0:
        n.append(p)
        p = float(input())
    implista(n)
    i = 0
    while i < len(n):
        if n[i] < 6.5:
            n.pop(i)
        else:
            i += 1
    print('\n')
    implista(n)
main()