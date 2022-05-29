listagem = ("Tênis", 99,
            "Blusa V", 69.90,
            "Short", 45.90,
            "Boné Adidas", 139.90,
            "Kimono", 298.90,
            "Bola de Fut Americano", 179.80,
            "Garrafa térmica", 40,
            "Camisa do Flamengo", 15.99,
            "Luva de boxe", 237.90)
print("-" * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("-" * 40)
for pos in range(0, len(listagem)):
      if pos % 2 == 0:
          print(f"{listagem[pos]:.<30}", end="")
      else:
          print(f"R${listagem[pos]:>7.2f}")
print("-" * 40)
