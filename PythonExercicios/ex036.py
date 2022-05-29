print("-"*25)
print("CAIXA ECONÔMICA FEDERAL")
print("-"*25)

valor = float(input("Qual o valor do imóvel desejado? R$"))
wage = float(input("Qual o eu salário atual? R$"))
tempo = int(input("Em quantos anos você deseja quitar o imóvel? "))

comprometimento = valor/(tempo*12)
comppct = (comprometimento/wage)*100

print("O financiamento compromete R${:.2f} do seu salário, representando dessa forma {:.2f}% dele.".format(comprometimento, comppct))
if comprometimento > wage * 0.30:
    print("Infelizmente não conseguimos aprovar esse valor no seu salário atual.")
    print("Que tal simularmos em {:.0f} anos?".format((valor/(wage*0.30))/12))
else:
    print("O valor foi pré-aprovado! O valor da parcela será {:.2f}. Aguarde o contato de seu gerente.".format(comprometimento))
