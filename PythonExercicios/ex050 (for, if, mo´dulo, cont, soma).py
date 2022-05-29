soma = 0
cont = 0
for a in range(1, 7):
    n = int(input("Digite o {}º número: ".format(a)))
    if n % 2 == 0:
        soma += n
        cont += 1

print("A soma dos {} números pares é {}.".format(cont, soma))
