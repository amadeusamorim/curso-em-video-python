#leia duas notas do aluno e calcule sua média

n1 = float(input("Digite sua nota qualitativa: "))
n2 = float(input("Digite sua nota da prova: "))
md= float ((n1+n2)/2)
aprovado = 7

print("Vamos aos resultados do bimestre:\n Qualitativa: {} \n Prova: {}\n Média: {:.1f}".format(n1, n2, md))
