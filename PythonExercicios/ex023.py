#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

número = (input("Digite um número entre 0 e 9999: "))
und = (número[3])
dez = (número[2])
cen = (número[1])
mil = (número[0])

print("Analisando seu número...")
print("Unidade: {}".format(und))
print("Dezena: {}".format(dez))
print("Centena: {}".format((número[1])))
print("Milhares: {}".format(mil))