''' 2. FAÇA UM PROGRAMA QUE LEIA UM NOME DE USUÁRIO E A SUA SENHA E NÃO ACEITE A SENHA IGUAL AO NOME DO USUÁRIO,
MOSTRANDO UMA MENSAGEM DE ERRO E VOLTANDO A PEDIR AS INFORMAÇÕES.'''

nome = str(input('Informe o nome: ')).strip()
senha = str(input('Informe a senha: ')).strip()
while nome == senha:
    senha = str(input('\033[1;31mPor favor usar senha diferente do nome\033[m. Digite uma nova senha: '))
print('\033[1;32mUsuário e senha cadstrado com sucesso!\033[m')
