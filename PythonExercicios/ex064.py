n = soma = 0
cont = -1
while n != 999:
    n = int(input("Digite um número [999 para parar]: "))
    cont += 1
    soma += n
print(f"Você digitou {cont} números e a soma entre eles foi {soma - 999}.")
