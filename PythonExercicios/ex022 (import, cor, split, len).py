# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.

#– Quantas letras ao todo sem considerar espaços.

#– Quantas letras tem o primeiro nome.

nome=str(input("Digite o seu nome completo: "))
a = nome.upper()
b = nome.lower()
c = (len(nome))
d = (nome.split())
e = len(d[0])
from time import sleep
print("\033[1;31mAnalisando seu nome...\033[m")
sleep(2)
print("Seu nome maiúsculo é {}.".format(a))
print("Seu nome minúsculo é {}.". format(b))
print("Seu nome tem {} letras.".format(c))
print("Seu primeiro nome possui {} letras.".format(e))