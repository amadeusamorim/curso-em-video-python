def escreva(txt):
    cabecalho = len(txt) + 6
    print("~"*cabecalho)
    print(f"{txt:^{cabecalho}}")
    print("~"*cabecalho)


escreva("OLÁ, MUNDO!")

escreva("AMA")
