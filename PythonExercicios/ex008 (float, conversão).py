#valor em metros, centimetros e milimetros

m = float(input("Quantos metros o senhor deseja? "))
cm = m*100
mm = m*1000

print("Metros de corda para venda:")
print("\nMetros: {}\nCentímetros: {:.2f}\nMilímetros: {:.2f}".format(m, cm, mm))