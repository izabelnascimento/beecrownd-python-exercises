from cmath import pi


d = int(input())
caixa = [int(c) for c in input().split()]

volumeBola = 4/3 * pi*pow(d/2, 3)
volumeCaixa = caixa[0]*caixa[1]*caixa[2]

if (volumeBola <= volumeCaixa and d <= caixa[0] and d <= caixa[1] and d <= caixa[2]):
    print("S")
else:
    print("N")
