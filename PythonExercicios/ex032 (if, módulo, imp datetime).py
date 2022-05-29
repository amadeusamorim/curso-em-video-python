#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import time
import datetime
ano = int(input("Que ano você quer analisar? Coloque 0 para analizar o ano atual. "))
print("PROCESSANDO...")
time.sleep(1)
if ano == 0:
    ano=datetime.date.today().year
if ano%4 == 0 and ano%100 != 0 or ano%400 == 00:
    print("O ano de {} É/foi bissexto.".format(ano))
else:
    print("O ano de {} NÃO é/foi bissexto.".format(ano))