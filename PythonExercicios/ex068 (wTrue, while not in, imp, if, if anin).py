from random import randint
from time import sleep
print("-="*20)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("-="*20)
soma = c = 0
escolha = ""
while True:
    comp = randint(0, 10)
    eu = int(input("Digite um valor: "))
    soma = comp + eu
    escolha = str(input("Par ou Ímpar? [P/I]: ")).strip().upper()[0]
    while escolha not in "PI":
        escolha = str(input("Par ou Ímpar? [P/I]: ")).strip().upper()[0]
    print("--"*20)
    sleep(1)
    if soma % 2 == 0:
        print(f"Você jogou {eu} e o computador jogou {comp}. A soma é {soma} e por consequência o número é PAR.")
    else:
        print(f"Você jogou {eu} e o computador jogou {comp}. A soma é {soma} e por consequência o número é ÍMPAR.")
    print("--"*20)
    if escolha == "P":
        if soma %2 == 0:
            print("Você VENCEU!")
            print("Vamos jogar novamente..")
            c += 1
            print("-=" * 20)
        else:
            print("Você PERDEU!")
            break
    elif escolha == "I":
        if soma %2 != 0:
            print("Você VENCEU!")
            print("Vamos jogar novamente..")
            c += 1
            print("-=" * 20)
        else:
            print("Você PERDEU!")
            break
print("-="*20)
print(f"GAME OVER! Você venceu {c} vezes.")
