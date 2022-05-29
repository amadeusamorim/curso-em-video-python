from math import factorial
print("*** Calculadora de \033[1:33mFatorial\033[m ***")
n = int(input("Digite um número: "))
f = factorial(n)
print(f"O fatorial de {n} é {f:,}.")
