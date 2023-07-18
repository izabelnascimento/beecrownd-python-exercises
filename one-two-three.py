t = int(input())

while (t > 0):
    palavra = input()
    if (len(palavra) == 3):
        if (palavra[0] == "o" or palavra[2] == "e"):
            print(1)
        else:
            print(2)
    else:
        print(3)
    t = t-1
