from time import sleep
def contador(início, fim, passo):
    print(f"Contagem de {início} até {fim} de {passo} em {passo}:")
    sleep(0.5)
    if fim > início and passo > 0:
        fim += 1
    if início > fim:
        fim -= 1
        if passo > 0:
            passo *= -1
    if passo == 0:
        passo = 1
    for c in range(início, fim, passo):
        print(c, end=" ", flush=True)
        sleep(0.3)
    print("FIM!")
    print("-="*20)


print("-="*20)
contador(1, 10, 1)
contador(10, 0, 2)
print("Agora é a sua vez de personalizar a contagem!")
ini = int(input("Início: "))
fim = int(input('Fim:    '))
pas = int(input("Passo:  "))
contador(ini, fim, pas)
