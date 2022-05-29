somaidade = 0
totalidade = 0
maioridadehomem = 0
nomevelho = ""
totmulher20 = 0
for pessoa in range(1, 5):
    print("----- {}ª PESSOA -----".format(pessoa))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    totalidade += 1
    if pessoa == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1
print("A média de idade das pessoas é {:.1f} anos.".format(somaidade/totalidade))
print("O homem mais velho tem {} anos e se chama {}.".format(maioridadehomem, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos.".format(totmulher20))
