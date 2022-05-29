num=int(input("vamo de número aqui: "))
db=num*2
tp=num*3
rq=num**(1/2)

print("Escolhi o {} e aqui vai algumas coisas sobre ele: \nDobro: {} \nTriplo: {} \nRaiz quadrada: {:.2f}".format(num, db, tp, rq))

#outro jeito

print("Outro jeito:\n Dobro: {}\n Triplo: {}\n RQ: {}".format(num*2, num*3, (num**(1/2))))