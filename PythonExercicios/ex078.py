from time import sleep
num = list()
mai = men = 0
for cont in range(0, 5):
    num.append(int(input(f"Digite um valor para a posição {cont}: ")))
    if cont == 0:
        mai = men = num[cont]
    else:
        if num[cont] > mai:
            mai = num[cont]
        if num[cont] < men:
            men = num[cont]
print("-="*20)
sleep(1)
print("Carregando lista...")
sleep(1)
print("-="*20)
print(f"Sua lista ficou dessa forma: {num}. \nMais precisamente assim:")
for c, v, in enumerate(num):
    print(f"O número {v} está na posição {c}.")
print("-="*20)
print(f"O MENOR valor escolhido foi {men} nas posições ", end="")
for i, v in enumerate(num):
    if v == men:
        print(f"{i}...", end="")
print(f"\nO MAIOR valor escolhido foi {mai} nas posições ", end="")
for i, v in enumerate(num):
    if v == mai:
        print(f"{i}...", end="")
