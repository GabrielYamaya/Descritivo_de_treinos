# %% [markdown]
# Exercício de operadores lógicos

# %%
from decimal import Decimal, getcontext
trabalho_terca = True
trabalho_quarta = False

tv50 = trabalho_terca and trabalho_quarta
tv32 = trabalho_terca != trabalho_quarta
sorvete = trabalho_terca or trabalho_quarta
saude = not sorvete

print("Tv50 = {}, Tv32 = {}, Sorvete = {}, Saúde = {}".format(
    tv50, tv32, sorvete, saude))
# da para trabalhar com índice também
print("Tv50 = {1}, Tv32 = {0}".format(tv32, tv50))

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

# %%
