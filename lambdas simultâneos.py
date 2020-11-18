"""
Crie duas funções  que sejam executadas simultâneamente,
uma delas tem de elevar os números da lista ao quadrado,
a outra ao cubo.
"""


    # ☾✿ Se define os valores que serão trabalhados pela lista:
numeros = [0, 1, 2, 3, 4]


    # ☾✿ São criadas dois lambdas(funções) que vão gerar listas de números em função de seus cubos ou quadrados:
func_2 = lambda i: list(map(lambda x: x**2, i))
func_3 = lambda i: list(map(lambda x: x**3, i))


    # ☾✿ As listas são apresentadas ao usuários:
print(func_2(numeros), func_3(numeros))
