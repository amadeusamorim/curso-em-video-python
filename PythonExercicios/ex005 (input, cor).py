#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input("Digite um número aqui: "))
n1 = num+1
n2 = num-1

print("O número escolhido foi \033[4;35m{}\033[m, seu sucessor é \033[4;31m{}\033[m e antecessor \033[4;32m{}\033[m.".format(num, n1, n2))

#jeito2

print("Reforçando, você escolheu {}, o número da frente é o {}  o de trás é o {}.".format(num, num+1, num-1))