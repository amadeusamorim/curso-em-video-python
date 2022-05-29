from random import randint # RESOLUÇÃO INTERMINADA - MT COMPLEXA
lista = list()
jogos = list()
print("-="*20)
print("{:^40}".format("JOGA NA MEGA"))
print("-="*20)
n = int(input("Quantos jogos você quer que eu sorteie? "))
tot = 1
while tot <= n:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
    print(f"Os números sorteados foram {lista}.")