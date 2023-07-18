import string

t = int(input())

i = 0
cont = 0
while (i < t):
    a, b = map(int, input().split())
    saida = ""
    while (a <= b):
        saida += str(a)
        a = a+1
    print(saida + saida[::-1])
    i = i+1
