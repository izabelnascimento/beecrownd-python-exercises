tesouros = []

while True:
    try:
        joia = input()
        if joia not in tesouros:
            tesouros.append(joia)
    except EOFError:
        break

print(len(tesouros))
