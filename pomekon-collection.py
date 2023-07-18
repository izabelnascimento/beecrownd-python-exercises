total = int(input())

i = 0
pokemons = []
while (i < total):
    pok = input()
    if (pok not in pokemons):
        pokemons.append(pok)
    i = i+1

print("Falta(m)", 151-len(pokemons), "pomekon(s).")
