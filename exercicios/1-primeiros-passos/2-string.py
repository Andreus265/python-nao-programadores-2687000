resumo = "Paloma é uma mulher de 46 anos que deseja mudar de profissão, por isso está estudando 'python'."

# Imprima na tela a variável "resumo"

print(resumo)

# Imprima na tela apenas a segunda letra da variável

print(resumo[1])

# Imprima na tela a idade de Paloma (resposta esperada: "46")

print(resumo[23:25])

# Imprima na tela o trecho final da variável

print(resumo[62:])

# Converta todos as letras para minúsculo e imprima na tela

print(resumo.upper())

# Converta todas as letras para maiúscula e imprima na tela

print(resumo.lower())

# Formate a frase para que a primeira letra de cada palavra seja maiúscula e imprima na tela

print(resumo.title())

# Formate a frase para que apenas a primeira letra da frase seja maiúscula e imprima na tela

palavras = resumo.split()
palavras_com_primeira_letra_minuscula = [palavra[0].lower() + palavra[1:] for palavra in palavras]
resumo_com_primeira_letra_minuscula = ' '.join(palavras_com_primeira_letra_minuscula)
print(resumo_com_primeira_letra_minuscula)

# Imprima na tela uma string utilizando uma variável, usando o recurso string format

print("Frase formatada:\n{}".format(resumo))
