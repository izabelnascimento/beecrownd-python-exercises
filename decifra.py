segredo = input()
cripto = input()

alfa = "abcdefghijklmnopqrstuvwxyz"
descripto = ""


def sequencia(letra):
    i = 0
    for l in alfa:
        if (letra == l):
            return i
        i = i+1


def troca(letra):
    j = 0
    for letra in segredo:
        if (j == seq):
            return letra
        j = j+1


for letra in cripto:
    seq = sequencia(letra)
    descripto = descripto + troca(letra)

print(descripto)
