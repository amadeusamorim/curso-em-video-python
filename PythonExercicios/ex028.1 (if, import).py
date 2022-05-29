from random import randint
from time import sleep
print("-=-"*50)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-"*50)
computador = randint(0, 5)
jogador = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(2)

if jogador == computador:
    print("Boa! Acertasse.")

else:
    print("GANHEI, pensei no número {} e não no {}. Fica pra próxima.".format(computador, jogador))