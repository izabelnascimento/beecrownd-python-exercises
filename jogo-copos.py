n = int(input())
moeda = input()

for i in range(0, n):
    movimento = int(input())
    if (movimento == 1):
        if (moeda == "A"):
            moeda = "B"
        elif (moeda == "B"):
            moeda = "A"
    elif (movimento == 2):
        if (moeda == "B"):
            moeda = "C"
        elif (moeda == "C"):
            moeda = "B"
    elif (movimento == 3):
        if (moeda == "A"):
            moeda = "C"
        elif (moeda == "C"):
            moeda = "A"

print(moeda)
