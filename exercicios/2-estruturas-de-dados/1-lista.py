# Crie uma lista apenas com elementos numéricos

lista_numerica = [10, 20, 30, 40, 50]

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora

lista_completa = ['Python', 42, True, [1, 2, 3], {'chave': 'valor'}]

# Imprima na tela apenas os 5 primeiros elementos da lista

print("Os 5 primeiros elementos da lista completa são:", lista_completa[:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par

print("Elementos de índice par da lista completa:", lista_completa[::2])

# Remova da lista o último item

lista_numerica.pop()
print("Lista numérica após remover o último item:", lista_numerica)

# Insira na lista um novo item

lista_numerica.append(60)
print("Lista numérica após inserir um novo item:", lista_numerica)

# Remova da lista um item específico

lista_completa.remove(42)
print("Lista completa após remover o item '42':", lista_completa)