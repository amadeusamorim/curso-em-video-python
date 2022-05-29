print("-----------------")
print("WSL 2021 Finals")
print("----------------")

surfista = str(input("Qual o surfista avaliado? "))
w1 = float(input("A melhor onda do {} foi: ".format(surfista)))
w2 = float(input("A segunda melhor onda do {} foi: ".format(surfista)))

nf = (w1+w2)/2

print("Os juízes deram notas {} e {} e {} ficou com média {}.".format(w1, w2, surfista, nf))