# %% [markdown]
# # Exemplos

# %%
print("Primeiro programa!")

# %%
1 + 5 + 6
5 + 8 + 9

# %%
print(1 + 5 + 6)
print(5 + 8 + 9)

# %% [markdown]
# # Tipos de variáveis

# %%
print("Booleana")
print(False)
print(True)
# Detalhe que precisa ter a inicial maiúscula

# %%
print("Float, int e double")
print(2.2 + 5 * 5.6669)

# %%
print("String")
print("Batata " + "Feijão " + 4 * "Arroz ")

# %%
print("Array ou lista")
print([1, 3, 4, "aceita varias variáveis"])
# trabalha com índice

# %%
print("Dicionário")
print({'nome': 'Pedrocas', 'idade': 22})
# trabalha com chave valor

# %%

# valor nulo

# %%
# A linguagem é dinamicamente tipada, ou seja, uma variável não é atrelada a um tipo de valor, como String ou int, então é possível fazer diferentes atribuições a uma mesma variável.
# A linguagem é altamente tipada, ou seja, o código sempre está ciente de qual valor está atribuído a uma variável a todo o tempo.

# %% [markdown]
# # Comentários

# %%
# ctrl + / comenta as linhas selecionadas

"""
awfawfaw

awdadadawwgr
"""

print(" as aspas duplas triplas também comentam ")

# %%
print(2 + 3)
print(1 - 2)
print(4 / 5)
print(8 * 9)
print(10.9 // 6)
print(5 ** 3)
print(8 % 3)

# %%
# Desafio cálculo de porcentagem
salario = 3056.99
despesas = 2059.66

comprometimento = despesas * 100 // salario
print(comprometimento)

# %% [markdown]
# # Operadores relacionais

# %%
3 > 8
3 >= 8
3 < 8
3 <= 3
3 != 8
3 == 3

# %% [markdown]
# # Operadores de atribuição

# %%
a = 3
a = a + 7

a += 8

# %%
a = 3
a = a - 2

a -= 2

# %%
a = 10
a = a / 2

a /= 2
a

# %%
a = 10
a = a * 2

a *= 10
a

# %%
a = 10

a %= 2
a

# %%
a = 2
a **= 3
a

# %%
a = 9
a //= 2
a

# %% [markdown]
# # Operadores lógicos

# %%
# Cuidado não confundir operdaores lógicos com operadores bit-a-bit

# %% [markdown]
# ## AND

# %%
print(7 != 3 and 2 > 3)
print(7 != 3 and 3 > 2)

# %% [markdown]
# ## OR

# %%
print(7 != 3 or 3 > 5)
print(7 != 7 or 3 > 2)
print(7 != 7 or 3 > 5)

# %% [markdown]
# ## XOR

# %%


def xor(x, y):
    return bool((x and not y) or (not x and y))


print(xor(7 != 7, 3 > 4))  # false    false = false
print(xor(7 != 2, 3 > 4))  # true     false = true
print(xor(7 != 7, 8 > 4))  # false    true = true
print(xor(7 != 2, 9 > 4))  # true     true = false

# %% [markdown]
# ## Negação (unário)

# %%
# inverte o sentido
print(not True)
print(not False)
print(not 0)
print(not 1)

# %% [markdown]
# ## Bit-a-bit

# %%
# Operadores bit-a-bit utilizam o valor binário de um um número, ou seja:
# 3 = 11, 1 = 1, 5 = 101, e assim vai.
# Dessa forma caso seja feita a seguinte operação:
print(3 & 4)
# O resultado será 000, pois será feito de seguinte forma: 100
#                                                          011
#                                                         -----
#                                                          000
print(5 & 4)

# O mesmo vale para os outros operadores:
print(3 | 2)
print(8 | 6)

print(3 ^ 2)
print(7 ^ 0)
print(7 ^ 5)

# %%
print("Error não existe mais")

# %% [markdown]
# Operadores ternários

# %%
esta_chovendo = True
'Hoje estou com as roupas ' + ('secas.', 'molhadas.')[esta_chovendo]
'Hoje estou com as roupas ' + ('molhadas.' if esta_chovendo else 'secas.')

# %% [markdown]
# Operador de identidade

# %%
lista = [1, 2, 3, 'Ana', 'Carla']
print(2 in lista)
print('Ana' not in lista)

# %% [markdown]
# Operador de identidade

# %%
x = 3
y = x
z = 3
print(x is y)
print(y is z)
print(z is not x)

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

print(lista_a is lista_b)
print(lista_a is lista_c)
print(lista_c is not lista_b)
# %% [markdown]
# Builtins

# %%
# esse é um módulo integrado do python que traz diversas funções
# como o print, type, dir, help, entre outros.

# %% [markdown]
# Conversão de tipos

# %%
# Para converter em python basta utilizar uma função que leve
# o nome do tipo com o valor a converter como parâmetro.

print(2 + int('4'))
print('Leia isso ' + str(59) + ' vezes')
print(2 + float('4.5'))

# detalhe que o valor a ser convertido precisa ser compatível.

# %%
# comando dir('tipo') exibe as possíveis funções que podem
# ser realizadas com ela
print(dir(int))

5.0.is_integer()
# %% [markdown]
# Números

# %%
from decimal import Decimal, getcontext
print(Decimal(1) / Decimal(7))

getcontext().prec = 4
print(Decimal(1) / Decimal(7))

print(Decimal.max(Decimal(1), Decimal(7)))

dir(Decimal)

# %% [markdown]
# Strings

# %%
dir(str)

nome = 'Saulo Pereira'
print(nome[0])
print(nome[-1])
print(nome[:3])
print(nome[:-3])
print(nome[3:])
print(nome[-3:])
print(nome[4:7])
print(nome[1:14:2])  # [início : Final : Passo]
print(nome[13:1:-2])
# nome[0] = 'P' Dá erro esse comando, não é possível alterar uma String, somente a variável.

# %%
# Maneiras de acrescentar um '  ou " no meio da String
"Dias D'Avila"
'Dias D\'Avila'
'Texto entre "aspas".'
"Texto entre \"aspas\"."

print("""Texto com múltiplas
linhas""")
print('''Texto com múltiplas
linhas''')
print("Texto com múltiplas\nLinhas")

# %%
frase = "Essa é uma frase de exemplo"
print("es" in frase)
print("Es" not in frase)

print(len(frase))
print(frase.lower())
print(frase)

frase = frase.upper()
print(frase)

print(frase.split())
print(frase.split('A'))

# dir(str)
# help(str.center)

# %% [markdown]
#Lista

# %%
lista = []
len(lista)
lista.append(3)

nova_lista = [2, 5.343, 'nome']
nova_lista.remove(2) #remove o elemento com valor 2
nova_lista.reverse()


lista2 = [2, 4, 5, 'Gjwd', 'adwa']
lista2.index(4)
2 in lista
lista2[2] #pega o indice 2
lista2[-2] #funciona também
lista2[1:3]
lista[1:-1]
dir(list)
# funciona como na string, mas há metodos também

# %% [markdown]
dir(tupla)
tupla = ('um')
type(tupla)
tupla = ('um', 2)
type(tupla)

tupla[1]

tupla.count('um')

# a principal diferença da tupla pra lista é que não dá para
# alterar um valor dentro de uma tupla, somente sobreescrevê-lo
# já na lista isso é possível 
# %% [markdown]
# Dicionários

# %%
pessoa = {'nome': 'Eduardo', 'idade': 32, 'cursos': ['da pra por outras', 'estruturas aqui']}
pessoa['cursos']
pessoa.keys()
pessoa.values()
pessoa.items()
pessoa['cursos'].append('Aqui também')
pessoa.pop('idade')
pessoa.update({'idade': 40, 'sexo': 'M'})
del pessoa['idade']
pessoa.clear()
pessoa
# %% [markdown]
# Conjunto

# %%
# não garante ordenação, não possue index e não armazena valores repetidos
a = {1, 2, 3}
a = set('codaaaarrr')
{1, 2, 3} == {3, 1, 2, 1}

# %%
c1 = {1, 2}
c2 = {2, 3}
c1.union(c2)
c1.intersection(c2)
c1 - c2

c1.update(c2)
c2 <= c1 #subconjunto


# %% [markdown]
# Interpolação

# %%
from string import Template
nome, idade = 'Ana', 39
print('Nome: %s Idade: %d' % (nome, idade)) #mais antigo
# %s espera uma String
# %d espera um inteiro
# %f espera um float, %.2f limita o número de casas

print('Nome: {0} Idade: {1}'.format(nome, idade)) #Python < 3.6

print(f'Nome: {nome} Idade: {idade}') #Python >= 3.6

s = Template('Nome: $nome Idade: $idade')
print(s.substitute(nome = nome, idade = idade))
