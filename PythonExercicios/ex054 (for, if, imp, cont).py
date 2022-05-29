import datetime
idade = datetime.date.today().year
old = 0
young = 0
for a in range(1, 8):
    nasc = int(input("Em que ano a {}ª pessoa nasceu? ".format(a)))
    if idade - nasc >= 18:
        old += 1
    else:
        young += 1
print("Ao todo tivemos {} pessoas MENORES de idade.".format(young))
print("E tivemos {} pessoas MAIORES de idade.".format(old))
