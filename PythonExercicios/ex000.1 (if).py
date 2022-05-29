n1 = "R$10.00"
n2 = "R$25.00"
n3 = "R$50.00"


print("---------------------------")
print("     CRIANÇA ESPERANÇA     ")
print("---------------------------")
print("Muito obrigado pelo contato!")
print("[1] para doar R$10")
print("[2] para doar R$25")
print("[3] para doar R$50")
print("[4] para doar outros valores")
print("[5] para cancelar")

doacao = int(input("Qual a opção desejada? "))

if doacao == 1:
    valor = 10
if doacao == 2:
    valor = 25
if doacao == 3:
    valor = 50
if doacao == 4:
    valor = float(input("Qual o valor da doação? R$"))
if doacao == 5:
    valor = 0
else:
    print("Opção inválida. Poderíamos começar novamente?")

print("---------------------------")
print("Sua doação foi de R${:.2f}".format(valor))
print("MUITO OBRIGADO!")
print("---------------------------")