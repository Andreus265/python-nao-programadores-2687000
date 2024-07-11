pessoa = {'nome':'Crislaine', 
          'idade':46, 
          'ano_formatura':2010, 
          'linguagens_programacao':['python', 'r', 'javascript', 'ruby'], 
          'brasileira':True, 
          'hobby':['nadar', 'ler', 'pedalar'], 
          'animal_estimacao':False}

# Imprima na tela o valor equivalente a chave "hobby"
print("hobby de Crislaine:", pessoa['hobby'])

# Imprima na tela uma lista apenas com os valores do dicionário

valores_dict = list(pessoa.values())
print("Lista de valores do dicionário pessoa:", valores_dict)

# Imprima na tela uma lista apenas com as chaves do dicionário

chaves_dict = list(pessoa.keys())
print("Lista de chaves do dicionário pessoa:", chaves_dict)

# Insira um novo par chave-valor no dicionário

pessoa['cidade'] = 'São Paulo'
print("Dicionário pessoa após inserção:", pessoa)