alt = float(input("Digite o sua altura: "))
peso = float(input("Digite o seu peso: "))
IMC = peso/(alt**2)

if IMC <= 17:
    print("Seu IMC é {:.2f}, constatando que você está muito abaixo do peso.".format(IMC))
elif IMC < 18.5:
    print("Seu IMC é {:.2f}, constatando que você está abaixo do peso.".format(IMC))
elif IMC < 25:
    print("Seu IMC é {:.2f}, constatando o seu peso ideal!".format(IMC))
elif IMC < 30:
    print("Seu IMC é {:.2f}, você está com sobrepeso.".format(IMC))
else:
    print("Seu IMC é {:.2f}, você está obeso e precisa se cuidar um pouco mais.".format(IMC))

