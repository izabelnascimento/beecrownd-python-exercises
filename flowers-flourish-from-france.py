frase = [""]


def isTautogram(frase, letra):
    for palavra in frase:
        if (palavra[0].lower() != letra or palavra[0] == "*"):
            return False
    return True


while (frase[0] != "*"):
    frase = [""]
    frase = input().split()

    letra = frase[0][0].lower()
    if (isTautogram(frase, letra)):
        print("Y")
    elif (frase[0] != "*"):
        print("N")
