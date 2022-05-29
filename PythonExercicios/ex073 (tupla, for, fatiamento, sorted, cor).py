brasileirao = ("Atletico Mineiro", "Palmeiras", "Fortaleza", "Flamengo",
               "Bragantino", "Internacional", "Corinthians", "Fluminense",
               "Atletico Goianiense", "América-MG", "Cuiabá", "Athletico-PR",
               "São Paulo", "Ceará", "Bahia", "Santos", "Juventude",
               "Sport", "Grêmio", "Chapecoense")

print("Os cinco primeiros colocados são:")
for cinco in brasileirao[:6]:
    print(cinco)
print("\nA zona de rebaixamento está formada por:")
for zona in brasileirao[16:]:
    print(zona)
print("\nOs atuais participantes do \033[0:33mBrasileirão\033[m são:")
for campeonato in sorted(brasileirao):
    print(campeonato)
print(f"\nA \033[0:32mChapecoense\033[m se encontra em {brasileirao.index('Chapecoense')+1}º lugar.")