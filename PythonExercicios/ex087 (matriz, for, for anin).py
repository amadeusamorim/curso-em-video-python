matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):  #lê a linha
    for c in range(0,3): #lê a coluna
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
print("-="*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end=" ")
        if matriz[l][c] % 2 == 0: #Elemento que acabou de ser exibido na tela é par?
            spar += matriz[l][c] #Se for, aí soma na tela
    print()
print("-="*30)
print(f"A soma dos valores pares da matriz é {spar}.")
for l in range (0, 3):
    scol += matriz[l][2] #A terceira coluna é representada pelo [2]
print(f"A soma dos valores da terceira coluna é {scol}.")
mai = max(matriz[1][0], matriz[1][1], matriz[1][2])
print(f"O maior valor da linha 2 é {mai}.")