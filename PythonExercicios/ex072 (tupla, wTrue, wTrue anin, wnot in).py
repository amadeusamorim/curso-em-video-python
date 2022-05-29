cont = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:
    while True:
        num = int(input("Digite um número entre 0 e 20: "))
        if 0 <= num <= 20:
            break
        print("Número inválido.", end = " ")
    print(f"Você digitou o número {num}, que por extenso é {cont[num]}.")
    resp = str(input("Quer continuar?: [S/N] ")).strip().lower()[0]
    while resp not in "sn":
        resp = str(input("Quer continuar?: [S/N] ")).strip().lower()[0]
    if resp == "n":
        break
print("="*40)
print("PROGRAMA ENCERRADO")
