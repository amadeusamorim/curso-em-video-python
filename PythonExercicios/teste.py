dados = {
    'Passat': {
        'ano': 2012,
        'km': 50000,
        'valor': 75000,
        'acessorios': ['Airbag', 'ABS']
    },
    'Crossfox': {
        'ano': 2015,
        'km': 35000,
        'valor': 25000
    }
}

# for carro in carros:
#     for item in carro[4]:
#         print(item)

var = 'acessorios' in dados['Crossfox']
print(var)

var2 = 'acessorios' in dados['Passat']
print(var2)