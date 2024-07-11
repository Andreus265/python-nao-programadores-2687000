# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.

# 1. Solicitar os dados da estudante
nome = input("Digite seu nome: ")
ano_conheceu_linkedin = int(input("Digite o ano que você conheceu o LinkedIn: "))
ano_atual = int(input("Digite o ano atual: "))
cursos = input("Digite os cursos realizados no LinkedIn Learning separados por vírgula (em ordem cronológica): ")

# Convertendo os cursos para uma lista
lista_cursos = cursos.split(',')

# 2. Armazenar os dados em um dicionário
estudante = {
    'nome': nome,
    'ano_conheceu_linkedin': ano_conheceu_linkedin,
    'ano_atual': ano_atual,
    'cursos': lista_cursos
}

# 3. Imprimir na tela as informações formatadas
total_anos_transcorridos = ano_atual - ano_conheceu_linkedin
primeiro_curso = lista_cursos[0].strip()
ultimo_curso = lista_cursos[-1].strip()
total_cursos_realizados = len(lista_cursos)

# Formatando a string com as informações
print(f"Nome: {estudante['nome']}")
print(f"Ano que conheceu o LinkedIn: {estudante['ano_conheceu_linkedin']}")
print(f"Total de anos transcorridos desde então: {total_anos_transcorridos} anos")
print(f"Total de cursos realizados: {total_cursos_realizados}")
print(f"Primeiro curso: {primeiro_curso}")
print(f"Último curso: {ultimo_curso}")