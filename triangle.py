import re

vetor = input().split()
vetor[0], vetor[1], vetor[2], vetor[3] = int(
    vetor[0]), int(vetor[1]), int(vetor[2]), int(vetor[3])

valido = False
i = 0
while (i < 4):
    j = i+1
    while (j < 4):
        k = j+1
        while (k < 4):
            if ((vetor[i] + vetor[j] > vetor[k]) and (vetor[k] + vetor[j] > vetor[i]) and (vetor[k] + vetor[i] > vetor[j])):
                valido = True
            k = k+1
        j = j+1
    i = i+1


if (valido == True):
    print("S")
else:
    print("N")
