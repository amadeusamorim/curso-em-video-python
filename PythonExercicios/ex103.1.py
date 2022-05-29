def mostra_ficha(jogador='<desconhecido>', gols=0):
    if not jogador:
        jogador = '<desconhecido>'
    while True:
        if not gols or not gols.isnumeric():
            gols = 0
            break
        if gols.isnumeric():
            gols = int(gols)
            break
    print(f'O jogador {jogador} fez {gols} gol(s) no camp.')

# Programa principal
while True:
    nomejogador = input('Nome do jogador: ').title()
    golsjog = input(f'Quantos gols o jogador fez? ')
    mostra_ficha(jogador=nomejogador, gols=golsjog)
