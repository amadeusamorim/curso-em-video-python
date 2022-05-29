print("=="*11)
print("10 TERMOS DE UMA PA")
print("=="*11)

primeiro = int(input("Digite o primeiro termo da PA: "))
razão = int(input("Digite a razão da PA: "))
décimo = primeiro + (10-1) * razão

for c in range(primeiro, décimo + razão, razão):
    print("{} ".format(c), end="→ ")
print("ACABOU")