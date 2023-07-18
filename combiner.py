t = int(input())

while (t > 0):

    palavras = input().split()
    nova = ""

    tam0 = len(palavras[0])
    tam1 = len(palavras[1])

    i = 0
    j = 0

    for m in range(tam0 + tam1):
        if ((m % 2 == 0 or i > tam1) and i < tam0):
            nova = nova + palavras[0][i]
            i = i+1
        elif (j < tam1):
            nova = nova + palavras[1][j]
            j = j+1

    print(nova)
    t = t-1
