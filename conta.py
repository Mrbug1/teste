from time import sleep
resp = ''
nsal = 0
lenb = list()
sad = 0
cont = 0
senh = ''
print('Crie sua conta no banco!')
print('instruções: o nome de usuario deve ter mais de 4 caracteres,')
print('a senha deve conter mais de 3 caracteres')
usuario = str(input('Digite o nome de usuario: ')).strip()
senha = str(input('Digite sua senha: ')).strip()
while len(senha) <= 3:
    print('Sua senhar é fraca!')
    senha = str(input('Digite uma senha mais forte: ')).strip()
    print('Verificando nova senha...')
    sleep(0.5)
print('Cadastro concluido com sucesso!')
print('===============================')
print('LOGIN ')
user = str(input('Digite seu nome de usuario: ')).strip()
senh = str(input('Digite sua senha: ')).strip()
while usuario != user or senh != senha:
    user = str(input('Digite seu nome de usuario: '))
    senh = str(input('Digite sua senha: '))
if user == usuario and senh == senha:
    while True:
        print('========================')
        print('     Dados Bancarios    ')
        print('========================')
        print('presione "1" para alterar o saldo.')
        print('Presione "2" para checar os lembretes.')
        print('Precione "3" para checar o saldo de Emergencia.')
        print('Precione "4" para sair')

        resp = input('Qual das opções acima? ')
        if resp == '1':
            print(f'Seu saldo atual é de R${nsal}')
            q = str(input('Deseja alterar o saldo? [S/N]')).upper()
            if q == 'S':
                print('Configurações de saldo')
                nsal = input('Informe seu novo saldo R$: ')
                print('Saldo atualizado!')
            elif q == 'N':
                pass
            else:
                print('Erro opção invalida.')
            sleep(0.4)
        elif resp == '2':
            print('LEMBRETES: ')
            print(lenb)
            print('=' * 20)
            print('[1] para adicionar.')
            print('[2] para apagar o lembre que será escolhido.')
            print('[3] Para voltar para o menu principal. ')
            w = input('Sua opção: ').upper().strip()
            if w == '1':
                lenb.append(str(input('Digite seus lembretes aqui: ')))
                cont += 1
                sleep(0.5)
                print('Salvo.')
            elif w == '2':
                print(lenb)
                q = int(input('Digite o numero do lembrete que desseja apagar: '))
                lenb.pop(q - 1)
            elif w == '3':
                pass
            else:
                print('ERRO! OPÇÃO INVALIDA.')
            sleep(0.5)
        elif resp == '3':
            print('Saldo de Emergencia: ')
            print(f'R${sad}')
            e = input('Deseja alterar: [S/N]').strip().upper()
            if e == 'S':
                sad = input('Digite aqui seu saldo de emergencia R$: ')
                print('Concluido')
                sleep(0.2)
            elif e == 'N':
                pass
            else:
                print('Opção invalida! tente novamente.')
            sleep(0.2)
        elif resp == '4':
            print('FERRAMENTAS: ')
            print('=' * 20)
            print('[1] Conversor')
            r = str(input('Opção: '))
            if r == '1':
                n = float(input('Digite o valor a ser convertido para R$: '))
                print('COnversor de moedas: ')
                print(f'Valor convertido de dólares americanos: {n * 5.11}')
                print(f'Valor convertido de Euros: {n * 5.55}')
                print('_' * 20)
        else:
            print('=' * 20)
            print(f'{"Volte sempre!":^}')
            print('=' * 20)
            exit()
