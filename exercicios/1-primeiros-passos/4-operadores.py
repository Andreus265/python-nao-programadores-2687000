ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura

idade_de_formatura= ano_formatura - ano_nascimento
print('A idade de Gerlaine durante a formatura é de:', idade_de_formatura)

# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas

comparacao_maior = ano_nascimento > ano_formatura
comparacao_menor_igual = ano_nascimento <= ano_formatura
comparacao_igual = ano_nascimento == ano_formatura

print(f'O ano de nascimento ({ano_nascimento}) é maior que o ano de formatura ({ano_formatura}): {comparacao_maior}')
print(f'O ano de nascimento ({ano_nascimento}) é menor ou igual ao ano de formatura ({ano_formatura}): {comparacao_menor_igual}')
print(f'O ano de nascimento ({ano_nascimento}) é igual ao ano de formatura ({ano_formatura}): {comparacao_igual}')

# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas

expressao_and = (ano_nascimento < 2000) and (ano_formatura > 2005)
expressao_or = (ano_nascimento < 2000) or (ano_formatura > 2020)
expressao_not = not (idade_de_formatura >= 25)
print(f'O resultado da expressão (ano_nascimento < 2000) and (ano_formatura > 2005) é: {expressao_and}')
print(f'O resultado da expressão (ano_nascimento < 2000) or (ano_formatura > 2020) é: {expressao_or}')
print(f'O resultado da expressão not (idade_de_formatura >= 25) é: {expressao_not}')