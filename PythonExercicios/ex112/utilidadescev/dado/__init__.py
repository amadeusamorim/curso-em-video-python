def leiaDinheiro(msg):
    valid = False
    while not valid:
        entrada = str(input((msg))).replace(',','.').strip()
        if entrada.isalpha() or entrada == "":
            print(f"\033[0;31mERRO! \"{entrada}\" não é um preço válido.\033[m")
        else:
            valid = True
            return float(entrada)
