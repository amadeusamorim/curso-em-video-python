from random import sample
from time import sleep
jogos = list()
print("-="*20)
print("{:^40}".format("JOGA NA MEGA"))
print("-="*20)
n = int(input("Quantos jogos você quer que eu sorteie? "))
print("-="*20)
print("-="*4, end="   ")
print(f"SORTEANDO {n} JOGOS", end="   ")
print("-="*4)
for c in range(n):
    a = sorted(sample(range(1, 61), 6))
    jogos.append(a[:])
    print(f"Jogo {c+1}: {a}")
    sleep(0.5)
print("-="*6, end="   ")
print("BOA SORTE", end="   ")
print("-="*6)