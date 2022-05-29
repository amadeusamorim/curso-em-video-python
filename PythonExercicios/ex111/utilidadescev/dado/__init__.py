def leiaDinheiro(p):
    while True:
        p = input(str(' '))
        if p.isnumeric():
            p = int
        else:
            print(f"ERRO! {p} não é um preço válido.")
