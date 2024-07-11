# Crie uma função para selecionar o curso desejado em uma trilha profissional

# Crie uma função para percorrer todos os níveis de um curso e imprimir na tela a informação do nível atual

# Execute as funções

def selecionar_curso(curso):
    return f"Curso selecionado: {curso}"
def percorrer_niveis_curso(curso):
    print(f"Níveis do curso '{curso}':")
    for nivel in range(1, 6):  
        print(f"Nível {nivel}: Informações do nível atual.")
curso_desejado = "Python para Ciência de Dados"
print(selecionar_curso(curso_desejado))
print("\nPercorrendo os níveis do curso:")
percorrer_niveis_curso(curso_desejado)