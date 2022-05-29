def ficha(nome="<desconhecido>", gols=0):
    print("-"*40)
    print (f"O jogador {nome} fez {gols} gol(s) no campeonato.")


print("-"*40)
jogador = str(input("Nome do Jogador: "))
g = str(input("Número de gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if jogador.strip() == "":
    ficha(gols=g)
else:
    ficha(jogador, g)
