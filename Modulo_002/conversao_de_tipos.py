# Float para Interio e Inteiro para Float
print('################')
preco = 500.83
quantidade = 38
print(type(preco), preco)

print('################')
preco = int(preco)
print(type(preco), preco)

print('################')
preco = preco / 2
print(type(preco), preco)

print('################')
preco = preco // 2
print(type(preco), preco)

print('################')
preco = str(preco)
print(type(preco), preco)

print('################')
preco = float(preco)
print(type(preco), preco)

print('################')
preco = float(preco) * quantidade
print(type(preco), preco)

print('################')
texto = f'Quantidade: {quantidade} - Preço: R$ {preco:,.2f}.'
print(texto)