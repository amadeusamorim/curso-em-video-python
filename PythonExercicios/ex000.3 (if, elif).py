print("-----------------------------")
print("       WELKOM SCHOOL         ")
print("-----------------------------")

grade1 = float(input("Primeira nota: "))
grade2 = float(input("Segunda nota: "))

avgrade = (grade1 + grade2)/2
if avgrade == 10.0:
    desempenho = "A+"
elif avgrade >=9.0:
    desempenho = "A"
elif avgrade >= 8.0:
    desempenho = "B"
elif avgrade >= 7.0:
    desempenho = "C"
elif avgrade >= 6.0:
    desempenho = "D"
elif avgrade >= 5.0:
    desempenho = "E"
else:
    desempenho = "F"
print("-----------------------------")
print("MÉDIA: {}".format(avgrade))
print("APROVEITAMENTO: {}".format(desempenho))
print("-----------------------------")