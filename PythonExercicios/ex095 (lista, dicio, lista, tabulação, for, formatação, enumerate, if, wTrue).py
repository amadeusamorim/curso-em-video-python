jogadores = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador["nome"] = str(input("Nome do jogador: ")).capitalize().strip()
    tot = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    partidas.clear()
    for c in range (0, tot):
        partidas.append(int(input(f"  Quantos gols na partida {c+1}? ")))
    jogador["gols"] = partidas[:]
    jogador["total"] = sum(partidas)
    jogadores.append(jogador.copy())
    while True:
        continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
        if continuar in "SN":
            break
        print("ERRO! Comando inválido, responda apenas com S ou N.")
    if continuar == "N":
        break
    print("-"*20)
print("-"*40)
print("cod ", end="")
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()
print("-"*40)
for k, v in enumerate(jogadores):
    print(f"{k:>3} ", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print("-"*40)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f"ERRO! Não existe jogador com o código {busca}!")
    else:
        print(f"  --  LEVANTAMENTO DO JOGADOR {jogadores[busca]['nome']}: ")
        for i, g in enumerate(jogadores[busca]["gols"]):
            print(f"    No jogo {i+1} fez {g} gols.")
    print("-" * 40)
print(" <<<<<< VOLTE SEMPRE >>>>>")
