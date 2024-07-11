data_nascimento = '05-10-1976'
idade_numerica = 46
altura = 1.74

# Descubra o tipo de dado de cada variável acima

tipo_data = type(data_nascimento)
tipo_idade = type(idade_numerica)
tipo_altura = type(altura)

print('altura é:',tipo_altura)
print('data é:',tipo_data)
print('idade é:',tipo_idade)

# Realize uma operação entre dados do tipo string e inteiro

idade_concatenada = data_nascimento + ' ' + str(idade_numerica)

print("Idade concatenada:", idade_concatenada)

# Realize uma operação entre dados do tipo inteiro e float

soma_idade_altura = idade_numerica + altura

print("Soma da idade com altura:", soma_idade_altura)