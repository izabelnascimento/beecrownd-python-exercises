import string

t = int(input())

x = 0
while (x < t):
    rajesh, sheldon = input().split(" ")

    if sheldon == rajesh:
        print("empate")
        x = x+1
    elif ((sheldon == "tesoura" and rajesh == "papel")
          or (sheldon == "papel" and rajesh == "pedra")
          or (sheldon == "pedra" and rajesh == "lagarto")
          or (sheldon == "lagarto" and rajesh == "spock")
          or (sheldon == "spock" and rajesh == "tesoura")
          or (sheldon == "tesoura" and rajesh == "lagarto")
          or (sheldon == "lagarto" and rajesh == "papel")
          or (sheldon == "papel" and rajesh == "spock")
          or (sheldon == "spock" and rajesh == "pedra")
          or (sheldon == "pedra" and rajesh == "tesoura")):
        print("sheldon")
        x = x+1
    elif ((rajesh == "tesoura" and sheldon == "papel")
          or (rajesh == "papel" and sheldon == "pedra")
          or (rajesh == "pedra" and sheldon == "lagarto")
          or (rajesh == "lagarto" and sheldon == "spock")
          or (rajesh == "spock" and sheldon == "tesoura")
          or (rajesh == "tesoura" and sheldon == "lagarto")
          or (rajesh == "lagarto" and sheldon == "papel")
          or (rajesh == "papel" and sheldon == "spock")
          or (rajesh == "spock" and sheldon == "pedra")
          or (rajesh == "pedra" and sheldon == "tesoura")):
        print("rajesh")
        x = x+1
