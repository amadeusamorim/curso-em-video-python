from time import sleep
from random import randint
num = list()
for cont in range(0, 5):
    num.append(randint(0,100))
print("-="*20)
sleep(1)
print("Carregando lista...")
sleep(1)
print("-="*20)
for c, v, in enumerate(num):
    print(f"Na posição {c} está o número {v}.")
print("-="*20)
print(f"O MENOR valor escolhido foi {min(num)}.")
print(f"O MAIOR valor escolhido foi {max(num)}.")
