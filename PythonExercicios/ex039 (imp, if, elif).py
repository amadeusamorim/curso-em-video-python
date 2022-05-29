import datetime
nasc = int(input("Qual o ano de seu nascimento? "))
ano = datetime.date.today().year-18
alist = nasc + 18
idade = ano - nasc
if ano > nasc:
    print("Já serviu a pátria? Fazem {} anos que você se alistou ou deveria ter se alistado.".format(ano-nasc))
    print("Seu alistamento foi em {}".format(alist))
elif ano < nasc:
    print("Opa, meu garoto. Faltam apenas {} anos para você se apresentar, prepara os documentos.".format(nasc-ano))
    print("Seu alistamento será em {}".format(alist))
elif ano == nasc:
    print("Hora de se alistar, procure a junta do exército mais próxima.")
