print("=-="*13)
print("Faculdade vc é fera")
print("=-="*13)
n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
media = (n1+n2)/2
print("Tirando {:.1f} e {:.1f}, sua média ficou {:.1f}".format(n1, n2, media))
if media >= 7:
    print("Parabéns, você foi \033[1:32mAPROVADO!\033[m")
elif media >= 5:
    print("Você está na \033[1:33mRECUPERAÇÃO\033[m.")
else:
    print("Você foi \033[1:31mREPROVADO\033.")