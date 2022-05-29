continua = ""
n = media = soma = c = menor = maior = 0
while continua != "N":
    n = int(input("Digite um número: "))
    soma += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continua = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
media = soma / c
print(f"Você digitou {c} números e a média foi {media:.2f}.")
print(f"O maior valor foi {maior} e o menor valor foi {menor}.")
