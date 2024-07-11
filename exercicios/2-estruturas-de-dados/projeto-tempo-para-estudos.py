# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.

nome = input('digite seu nome:')
total_dias = int(input('digite o total de dias dedicados ao estudo por semana:'))
total_horas = int(input('digite a media de horas dedicadas ao estudo por dia:'))
curso = input('titulo do curso que está cursando:')

print(f'ola{nome}, voce costuma estudar {total_dias} dias por semana com uma média de {total_horas} horas por dia para realizar o curso {curso}. ')