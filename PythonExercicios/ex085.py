numeros = list()
pares = list()
impares = list()
for n in range(0, 7):
    numeros.append(int(input(f"Digite o {n+1}º número: ")))
print("-="*30)
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f"Os números pares digitados foram: {sorted(pares)}.")
print(f"Os números ímpares digitados foram: {sorted(impares)}.")
