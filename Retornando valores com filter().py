"""
Retornando apenas valores negativos entre -5 e 5 através da função filter():
"""

    # ☾✿ A lista é criada começando do -5 e parando 1 index antes do 6:
valores = list(range(-5, 6))

    # ☾✿ São filtrados em "resultado" apenas os elementos de "valores" maiores que 0:
resultado = list(filter(lambda x : x < 0 , valores))

    # ☾✿ A lista é apresentada ao usuário:
print(resultado)
