alt = float(input("Qual a sua altura? (m) "))
peso = float(input("Qual o seu peso? (Kg) "))
IMC = peso/(alt**2)
print("Seu IMC é de {:.1f}.".format(IMC))
if IMC <= 17:
    print("Você está MUITO ABAIXO DO PESO.")
elif IMC <= 18.5:
    print("Você está ABAIXO DO PESO.")
elif IMC <= 25:
    print("Você está no seu PESO IDEAL!")
elif IMC <= 30:
    print("Você está com SOBREPESO.")
elif IMC <= 40:
    print("Você está com OBESIDADE, cuidado!")
else:
    print("Você está OBESIDADE MÓRBIDA, cuidado")