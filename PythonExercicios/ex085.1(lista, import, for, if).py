from random import randint
num = [[], []]
valor = 0
for n in range(1, 8):
    valor = randint(0, 299) #coloquei isso pra n ficar digitando direto os input, nam
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print("-="*30)
num[0].sort()
num[1].sort()
print(f"Os números pares digitados foram: {num[0]}.")
print(f"Os números ímpares digitados foram: {num[1]}.")
