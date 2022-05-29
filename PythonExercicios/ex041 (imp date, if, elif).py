from datetime import date

print("\033[1:34m~~\033[m"*16)
print("\033[7:34mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m")
print("\033[1:34m~~\033[m"*16)

nasc = int(input("Ano de nascimento: "))
hoje = date.today().year
idade = hoje - nasc
print("O atleta tem {} anos.".format(idade))
print("SUA CLASSIFICAÇÃO É:")
if idade <= 9:
    print("\033[1mMIRIM\033[m")
elif idade <= 14:
    print("\033[1mINFANTIL\033[m")
elif idade <= 19:
    print("\033[1mJUNIOR\033[m")
elif idade <= 20:
    print("\033[1mSENIOR\033[m")
else:
    print("\033[1mMASTER\033[m")