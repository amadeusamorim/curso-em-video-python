print("==="*15)
print("{:^45}".format("BANCO DO AMA"))
print("==="*15)
v = c50 = m50 = c20 = m20 = c10 = m10 = c1 = 0
while True:
    v = int(input("Que valor você quer sacar? R$"))
    c50 = v // 50
    m50 = v % 50
    c20 = m50 // 20
    m20 = m50 % 20
    c10 = m20 // 10
    m10 = m20 % 10
    c1 = m10 // 1
    if c50 != 0:
        print(f"Total de {c50} notas de R$50.")
    if c20 != 0:
        print(f"Total de {c20} notas de R$20.")
    if c10 != 0:
        print(f"Total de {c10} notas de R$10.")
    if c1 != 0:
        print(f"Total de {c1} notas de R$1.")
    print("===" * 15)
    break
print("Volte sempre ao BANCO DO AMA. Tenha um bom dia!")
