t = int(input())

while (t > 0):
    comida = float(input())
    dia = 0
    while (comida > 1):
        comida = comida/2
        dia = dia+1
    print(dia, "dias")
    t = t-1
