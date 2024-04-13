# Função de entrada de dados
nome = input('Informe o seu nome: ')
sobrenome = input('Informe o seu sobrenome: ')
idade = input('Informe a sua idade: ')

# Função de saída de dados
# Argumentos opcionais: sep, end e file
print(nome, sobrenome)
print(nome, sobrenome, sep="#")
print(nome, sobrenome, end="...\n")
print(nome, sobrenome, sep="#", end="...\n")

with open('Modulo_002/funcoes_saida.txt', 'w') as f:
    print(f'Nome: {nome} {sobrenome} - Idade: {idade} anos.', file=f)