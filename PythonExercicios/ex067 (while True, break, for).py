n = 0
while True:
    n = int(input("Quer ver a tabuada de qual valor? "))
    if n < 0:
        break
    print("-"*40)
    for a in range(1, 11):
        print(f"{n} x {a:2} = {n*a}")
    print("-"*40)
print("-"*40)
print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")
