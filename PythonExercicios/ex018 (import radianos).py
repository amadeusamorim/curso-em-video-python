#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ang=float(input("Digite o ângulo que você deseja: "))
sn= math.sin(math.radians(ang))
co= math.cos(math.radians(ang))
tg=math.tan(math.radians(ang))

print("O ângulo de {} tem o SENO de {:.2f}".format(ang, sn))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(ang, co))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(ang, tg))