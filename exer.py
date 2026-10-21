
def temp(s):
    h = s//3600
    resto = s%3600
    m = resto//60
    s = resto%60
    print(f"{h}:{m}:{s}")

def main():
    seg = int(input(""))
    temp(seg)
main()