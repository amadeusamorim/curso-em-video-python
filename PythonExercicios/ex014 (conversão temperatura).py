# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input("Informe a temperatura em °C: "))
f = 9 * celsius / 5 + 32 #ordem de precedência nao precisa de parenteses

print("A temperatura de {}°C, corresponde a {:.1f}°F".format(celsius, f))
