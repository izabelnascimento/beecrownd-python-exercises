letra = input()
texto = input().split()


def isPalavra(palavra):
    if letra in palavra:
        return True
    return False


i = 0
cont = 0
for palavra in texto:
    if (isPalavra(palavra)):
        i = i+1
    cont = cont+1

percentual = 100*i/cont
print("%.1f" % percentual)
