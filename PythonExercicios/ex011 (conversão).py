#ler altura e largura e area + tinta necessária

altura=float(input("Qual a altura da parede? "))
largura=float(input("Qual a largura da parede? "))
mq=altura*largura
tinta=mq/2

print("Levando em consideração que a parede do senhor tem {:.2f} metros quadrados, vou precisar de {:.1f} litros de tinta".format(mq, tinta))