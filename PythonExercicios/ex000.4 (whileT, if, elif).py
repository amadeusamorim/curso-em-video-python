print("***************************************")
print("             RECEPCIONISTAS            ")
recep = continuar = ""
ocup = 0
while True:
    print("***************************************")
    ocup = float(input("Qual a ocupação de hoje? [%] "))
    recep = str(input("Qual o recepcionista do dia? ")).strip().upper()
    while recep not in "NICOLASGISELELINDEMBERGSAMUELVERONICASUHELEN":
        recep = str(input("Qual o recepcionista do dia? ")).strip().upper()
    if ocup < 70:
        if recep in "NICOLAS":
            print("relaxa, pai")
        elif recep in "GISELE":
            print("avise pra camareira montar os sofá cama")
        elif recep in "LINDEMBERG":
            print("aqui ta meio bagunçado")
        elif recep in "SAMUEL":
            print("vo toma um gatorade")
        elif recep in "VERONICA":
            print("early in? claaro!")
        elif recep in "SUHELEN":
            print("hoje luan nao me deixou dormir")
        else:
            print("que?")
    else:
        if recep in "NICOLAS":
            print("kd a comida de dona ge pra ajudar o pai")
        elif recep in "GISELE":
            print("~~ abre o grupo da recepção: 'hello, people' 'então...'")
        elif recep in "LINDEMBERG":
            print("aqui é meio bagunçado")
        elif recep in "SAMUEL":
            print("o sistema bugou e deu checkin no 309 oxen")
        elif recep in "VERONICA":
            print("consigo um late out até 20h sem problemas!")
        elif recep in "SUHELEN":
            print("mais um over? meu pai eterno")
        else:
            print("que?")
    continuar = str(input("Você quer continuar? [S/N] ")).strip().upper()[0]
    while continuar not in "SsNn":
        continuar = str(input("Você quer continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
            break