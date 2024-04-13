"""
Exemplos de variáveis

Por convenção, utilizamos o padrão 'Snake Case' e sempre utilizando nomes sugestíveis, para dar nome as variáveis.
"""

#################
# Atribuindo valor para variáveis

age = 38
name = 'Müller'
surname = 'Nocciolli'
full_name = name +' '+ surname

print(f'Meu nome é {full_name} e eu tenho {age} ano(s) de idade.')


#################
# Atribuindo valor para variáveis em uma única linha

age, name, surname = (38, 'Müller', 'Nocciolli')
full_name = name +' '+ surname

print(f'Meu nome é {full_name} e eu tenho {age} ano(s) de idade.')


#################
# Alterando o valor de uma variável

age = 39
name = 'Müller'
surname = 'Ribeiro'
full_name = name +' '+ surname

print(f'Meu nome é {full_name} e eu tenho {age} ano(s) de idade.')



"""
O Python não tem uma palavra para indicar que a variável é uma constante, mas por convenção, utilizamos o padrão 'Snake Case', nome sugestívo e o nome da variável todo em letra maiúscula.
"""

#################
# Criando uma constante

DEBUG = True
BRAZILIAN_STATE = ['RJ', 'SP', 'MG', 'RS']
PATH = '/home/user/'