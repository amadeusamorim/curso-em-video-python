from random import randint
comp = randint(1, 10)
palpite = 0
tentativas = 1
while palpite != comp:
    palpite = int(input("Digite um número entre 1 e 10: "))
    if palpite != comp:
        tentativas += 1
        if palpite > comp:
            print("Menos...")
        else:
            print("Mais...")
    else:
        print("Parabéns, você acertou, o número procurado era o {}.".format(comp))
print(f"Você acertou na {tentativas}ª tentativa.")
