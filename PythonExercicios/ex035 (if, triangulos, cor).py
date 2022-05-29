#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print(("-=-")*40)
print("ANALISADOR DE TRIÂNGULOS")
print("-=-"*40)

s1 = float(input("Primeiro segmento: "))
s2 = float(input("Segundo segmento: "))
s3 = float(input("Terceiro segmento: "))

if s1<s2+s3 and s2< s1+s3 and s3<s1+s2:
    print("Os segmentos \033[1;32mPODEM\033[m formar um triângulo!")

else:
    print("Os segmentos \033[1;31mNÃO PODEM\033[m formar um triângulo.")