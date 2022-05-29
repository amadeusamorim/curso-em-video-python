from random import randint
from time import sleep
def sorteia(lista):
    print("Sorteando os 5 valores da lista: ", end="")
    for c in range(0, 5):
        numero = randint(1, 100)
        print(numero, end=" ")
        pool.append(numero)
        sleep(0.4)
    print("PRONTO!")


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"Somando os valores pares de {lista}, temos {soma}.")

pool = list()
sorteia(pool)
somaPar(pool)
