print("-=-"*25)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-"*25)

import random

dado = [0, 1, 2, 3, 4, 5]
sorteado = random.choice(dado)
n = int(input("Em que número eu pensei? "))

if n == sorteado:
    print("BOA, GAROTO!")

else:
    print("Ops, não foi dessa vez, amigo.")

print("O número escolhido pelo computador foi o {}.".format(sorteado))