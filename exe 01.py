''' 1. FAÇA UM PROGRAMA QUE PEÇA UMA NOTA, ENTRE ZERO E DEZ.
MOSTRE UMA MENSAGEM CASO O VALOR SEJA INVÁLIDO E CONTINUE PEDINDO ATÉ QUE O USUÁRIO INFORME UM VALOR VÁLIDO.'''

nota = int(input('Informe uma nota de 0 a 10: '))
while nota < 0 or nota > 10:
    nota = int(input('\033[1;31mDigito inválido! Informe um N° de 0 a 10:\033[m '))
print(f'O N° informado foi \033[1;33m{nota}\033[m!')
