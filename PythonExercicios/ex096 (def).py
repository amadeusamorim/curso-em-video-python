def área(largura, comprimento):
    a = largura * comprimento
    print(f"A área de um terreno {largura} x {comprimento} é de {a}m².")

print("-" * 30)
print("Controle de Terrenos")
print("-" * 30)
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))
área(l, c)
