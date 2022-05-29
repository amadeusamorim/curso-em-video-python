#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input("Qual a distância da sua viagem? "))
print("Você está prestes a fazer uma viagem de {}Km".format(dist))

if dist <=200:
    print("O preço de sua passagem é R${:.2f}".format(dist*0.50))
else:
    print("O valor de sua passagem é R${:.2f}!".format(dist*0.45))
print("Boa viagem!")