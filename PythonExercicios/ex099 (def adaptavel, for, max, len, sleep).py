from time import sleep
def maior(* valores):
    print("Analisando os valores passados...")
    for v in valores:
        print(f"{v}", end=" ", flush=True)
        sleep(0.2)
    print(f"\nForam informados {len(valores)} valores ao todo.")
    print(f"O maior valor informado foi {max(valores)}.")
    print("-="*30)
    sleep(1)


print("-="*30)
maior(5, 9, 12, 1, 0)
maior(3, 2, 777)
maior(13, 12)