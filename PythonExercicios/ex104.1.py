def leiaInt(num):
    print("-"*40)
    while True:
        valor = str(input(num))
        if valor.isnumeric():
            return valor
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido!\033[m")
            print("-" * 40)

#Programa principal
n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}.")
