"""
Faça com que os números da lista A recebam exponenciais da lista B!
"""

    # ☾✿ As listas são atribuídas as variáveis lA e lB:
lA = [2, 2, 2]
lB = [7, 3, 4]

    # ☾✿ É feita a atribuição de uma lista com os valores de lA^(elevados)
    #    aos valores de lB através de list comprehension
exp = [n**lB[i] for i, n in enumerate(lA)]

    # ☾✿ A lista é apresentada ao usuário:
print(exp)
