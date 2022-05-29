print("=="*11)
print("10 TERMOS DE UMA PA v2")
print("=="*11)
n1 = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
decimo = n1 + (10-1) * r
while n1 != decimo:
    n1 += r
    print(f"{n1} ", end="→ ")
print("FIM")
