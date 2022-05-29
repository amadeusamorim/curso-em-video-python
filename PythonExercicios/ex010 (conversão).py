#conversor de real em dólar

real=float(input("Tá com quanto de grana na carteira? "))
dolar= real/5.38

print("Com R${} na carteira, eu consigo uns U${:.2f}.".format(real, dolar))