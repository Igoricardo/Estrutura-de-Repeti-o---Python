''' 3. FAÇA UM PROGRAMA QUE LEIA E VALIDE AS SEGUINTES INFORMAÇÕES:
    A. NOME: MAIOR COM 3 CARACTERES
    B. IDADE: ENTRE 0 E 150
    C. SALÁRIO: MAIOR QUE ZERO
    D. SEXO: 'F' OU 'M'
    E. ESTADO CIVIL: 'S', 'C', 'V', 'D' '''

while True:
    print('-'*80)
    nome = str(input('NOME: ')).strip().title()
    idade = int(input('IDADE: '))
    salário = float(input('SALÁRIO: R$'))
    sexo = str(input('SEXO [\033[1;34mM = MASCULINO\033[m / \033[1;35mF = FEMININO\033[m]: ')).strip().upper()
    estado_civil = str(input('ESTADO CIVIL [S = SOLTEIRO(A) / C = CASADO(A) / V = VIÚVO(A) / D = DIVORCIADO(A)]: ')).strip().upper()
    print('-'*80)
    print('\033[1;32mRELATÓRIO DE INFORMAÇÕES\033[m')
    print('-'*80)
    if len(nome) > 3:
        print(f'O nome informado foi {nome} e é maior que 3 caracteres.')
    else:
        print(f'O nome informado foi {nome} e é menor que 3 caracteres.')
    if idade >= 0 and idade <= 150:
        print(f'A idade informada é {idade} anos e está entre 0 e 150 anos.')
    else:
        print(f'A idade informada é {idade} anos e não está dentro de 0 a 150 anos.')
    if salário > 0:
        print(f'O salário informado é R${salário:.2f}, portanto é maior que 0.')
    if sexo == 'M':
        print('O sexo informado foi \033[1;34mMasculino\033[m')
    else:
        print('O sexo informado foi \033[1;35mFeminino\033[m')
    if estado_civil == 'S':
        print('E seu estado civil é Solteiro(a)')
    elif estado_civil == 'C':
        print('E seu estado civil é Casado(a)')
    elif estado_civil == 'V':
        print('E seu estado civil é Viúvo(a)')
    elif estado_civil == 'D':
        print('E seu estado civil é Divorciado(a)')