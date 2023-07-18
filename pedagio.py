kms = [int(k) for k in input().split()]
custos = [int(p) for p in input().split()]

qtdPedagio = int(kms[0] / kms[1])
custoTotal = kms[0]*custos[0] + qtdPedagio*custos[1]

print(custoTotal)
