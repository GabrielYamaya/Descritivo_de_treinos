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

