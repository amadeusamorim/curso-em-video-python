frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print("Temos um palíndromo!")
    print(f"O inverso de {junto} é {inverso}.")
else:
    print("A frase digitada não é um palíndromo!")