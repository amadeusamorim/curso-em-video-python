def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return n


num1 = leiaInt("Digite um número Inteiro: ")
num2 = leiaFloat('Digite um número Real: ')
print(f"O valor inteiro digitado foi {num1} e o Real foi {num2}.")
