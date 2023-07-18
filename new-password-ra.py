t = int(input())

numeros = [('0', 'G', 'Q', 'a', 'k', 'u'),
           ('1', 'I', 'S', 'b', 'l', 'v'),
           ('2', 'E', 'O', 'Y', 'c', 'm', 'w'),
           ('3', 'F', 'P', 'Z', 'd', 'n', 'x'),
           ('4', 'J', 'T', 'e', 'o', 'y'),
           ('5', 'D', 'N', 'X', 'f', 'p', 'z'),
           ('6', 'A', 'K', 'U', 'g', 'q'),
           ('7', 'C', 'M', 'W', 'h', 'r'),
           ('8', 'B', 'L', 'V', 'i', 's'),
           ('9', 'H', 'R', 'j', 't')]


def acharDigito(l):
    for numero in numeros:
        for letra in numero:
            if (letra == l):
                return numero[0]


while (t > 0):
    senha = input()
    digitos = ''
    for l in senha:
        if (l != ' ') and (len(digitos) < 12):
            digitos = digitos + acharDigito(l)
    print(digitos)
    t = t-1
