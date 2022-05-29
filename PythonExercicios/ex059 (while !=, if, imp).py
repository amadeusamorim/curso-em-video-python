from time import sleep
print("*********** Calculadora especial do Ama ***********")
v1 = int(input("Digite seu primeiro valor: "))
v2 = int(input("Digite seu segundo valor: "))
escolha = 0
soma = 0
mult = 0
while escolha != 5:
    print(""" MENU DO AMA:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa""")
    escolha = int(input(">>>>>> Escolha uma opção acima: "))
    if escolha == 1:
        soma = v1 + v2
        print("O resultado da sua soma entre {} + {} é {}.".format(v1, v2, soma))
    elif escolha == 2:
        mult = v1 * v2
        print("O resultado da multiplicação entre {} x {} é {}.".format(v1, v2, mult))
    elif escolha == 3:
        if v1 > v2:
            print("{} é maior que {}.".format(v1, v2))
        else:
            print("{} é menor que {}.".format(v1, v2))
    elif escolha == 4:
        print("Ok, vamos iniciar novamente. Escolha novos números.")
        v1 = int(input("Digite qual seu \033[0:32mnovo\033[m primeiro número? "))
        v2 = int(input("Digite qual o seu \033[0:32mnovo\033[m segundo número? "))
    elif escolha == 5:
        print("Saindo da aplicação...")
        sleep(1)
    else:
        print("Opção inválida, tente novamente.")
    print("=-=" * 10)
    sleep(1)
print("Fim do programa. Volte sempre!")
