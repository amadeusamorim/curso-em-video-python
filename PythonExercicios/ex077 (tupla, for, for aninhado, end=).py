palavras = ("igreja", "biblia", "pastor", "ovelha", "Jesus",
            "Paulo", "espirito santo", "meditar", "evangelho",
            "amor", "sabedoria", "Salmos", "liderança", "Verbo da Vida")
for p in palavras:
    print(f"\nNa palavra {p.upper()} temos ", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=" ")
