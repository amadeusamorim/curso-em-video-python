#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input("Qual a velocidade do carro? "))
multa = 7 * (velocidade-80)
if velocidade > 80:
    print("VOCÊ FOI MULTADO! O limite da pista era 80 km/h, contudo sua velocidade estava a {}". format(velocidade))
    print("O valor de sua multa é R${:.2f}".format(multa))
print("Tenha um bom dia e dirija em segurança!")