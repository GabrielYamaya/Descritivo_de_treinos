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
