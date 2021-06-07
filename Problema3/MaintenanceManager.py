'''*******************************************************************************
Autor: Letícia Teixeira Ribeiro dos Santos
Componente Curricular: Algoritmos I
Concluido em: 05/06/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************'''


import os
from datetime import date, datetime, timedelta
import csv



# Verifica se já existe diretório de manutenções, se não, cria junto com o restante
def existeDir():
    if os.path.exists('Manutencoes') == False:
        os.makedirs('./Manutencoes')
        os.makedirs('./RegistroSistema')
        os.makedirs('./BalancoMensal')
        open('RegistroSistema/registro_clientes.txt', 'w', encoding='utf-8')
        open('RegistroSistema/registro_manut_agenda.txt', 'w', encoding='utf-8')
        open('RegistroSistema/registro_manut_realizada.txt', 'w', encoding='utf-8')



# Cadastra novos clientes
def cadastrarClientes(infoClientes):

    nome = input('Nome do cliente: ')
    endereco = input('Endereço: ')
    tel = input('Telefone: ')

    lerArquivo()  # Abre arquivo em modo de leitura adicionando em lista

    codClientes = len(infoClientes)   # Lê o tamanho da lista para incrementar código
    codClientes += 1

    clientes_temp = [nome, endereco, tel, codClientes] 

    with open('RegistroSistema/registro_clientes.txt', 'a') as arq:
        for dados in clientes_temp:
            dados = str(dados)
            arq.write(dados + ';')
        arq.write('\n')

    os.system('clear')
    print('Cliente cadastrado!\n')
    clientes_temp.clear()
    infoClientes.clear()



# Edita ou exclue clientes com base no código
def editCliente(infoClientes, infoManuts):

    lerArquivo()
    lerArquivoManut()
 
    opcao = int(input('[1] Editar \n[2] Excluir: '))
    cod = input('Informe o código do cliente: ')
    aux = 0

    # Alteração de informações e tratamento caso seja escolhido dado não editável ou inexistente
    if opcao == 1:
        for cliente in infoClientes:
            if cliente['codigo'] == cod:
                print('Digite o dado que deseja alterar. Opções: nome, endereço, telefone: ')
                dado = input().lower()
                if dado in ['nome', 'endereço', 'telefone']:
                    novodado = input('Digite o novo dado: ')
                    cliente[dado] = novodado
                    aux = 1
                    os.system('clear')
                    print('Dado alterado com sucesso!\n')
                if dado == 'codigo':
                    aux = 1
                    os.system('clear')
                    print('Não é possível alterar o código dos clientes! Tente novamente.\n')
        if aux == 0:
            print('Código inexistente!\n')

    # Exclusão verificando se está atrelado ou não a manutenção
    elif opcao == 2:
        for manutencao in infoManuts:
            if manutencao['id_cliente'] == cod:
                os.system('clear')
                print(f'Não é possivel remover cliente de código {cod}, está atrelado a manutenção!\n')
                aux = 1
        else:
            for cliente in infoClientes:
                if cliente['codigo'] == cod and aux == 0:
                    infoClientes.remove(cliente)
                    os.system('clear')
                    print('Cliente excluído.\n')
                

    # Alterações são sobrescritas no arquivo
    with open('RegistroSistema/registro_clientes.txt', 'w') as arq:
        for cliente in infoClientes:
            for dado in cliente.values():
                dado = dado + ';'
                arq.write(dado)
            arq.write('\n')   
            
    infoClientes.clear()
    infoManuts.clear()

# Menu com repetição e saída inicial para o usuário
def menuPrincipal():

    existeDir()
    
    iterador = 0

    while iterador == 0:
        print('=' * 30)
        print('» MENU «'.center(30))
        print('Insira o número correspondente')
        print('=' * 30)
        print('\n× CLIENTES')
        print('[1] Cadastrar \n[2] Listar \n[3] Excluir ou Editar \n')
        print('\n× MANUTENÇÕES')
        print('[4] Agendar \n[5] Editar ou Excluir \n[6] Realizar \n[7] Listar \n[8] Balanço Mensal \n[9] Sair')
        opcao = int(input())
        if opcao == 1:
            cadastrarClientes(infoClientes)
        elif opcao == 2:
            listarClientes(infoClientes)
        elif opcao == 3:
            editCliente(infoClientes, infoManuts)
        elif opcao == 4:
            agendaManutencao(infoManuts)
        elif opcao == 5:
            editManut(infoManuts)
        elif opcao == 6:
            realizarManut(infoManuts)
        elif opcao == 7:
            listarManut(infoManuts)
        elif opcao == 8:
            balancoMensal(infoManuts)
        elif opcao == 9:
            print('Programa finalizado.')
            iterador = 1
        elif opcao < 1 or opcao > 9:
            print('\nDigite uma opção válida!\n')


# Lê informações do arquivo de clientes e adiciona em uma lista de dicts
def lerArquivo():   
    with open('RegistroSistema/registro_clientes.txt', 'r') as arq:
        for linha in arq:
            dictCliente = {}
            linha = linha.rstrip().split(';')
            dictCliente['nome'] = linha[0]
            dictCliente['endereço'] = linha[1]
            dictCliente['telefone'] = linha[2]
            dictCliente['codigo'] = linha[3]
            infoClientes.append(dictCliente)

# Lê arquivo de manutenções agendadas e adiciona em lista de dicts
def lerArquivoManut():
    with open('RegistroSistema/registro_manut_agenda.txt', 'r') as arq:  
        for linha in arq:
            dictManut = {}
            linha = linha.rstrip().split(';')
            dictManut['data'] = linha[0]
            dictManut['valor'] = linha[1]
            dictManut['peça'] = linha[2]
            dictManut['validade'] = linha[3]
            dictManut['id_cliente'] = linha[4]
            dictManut['codigo'] = linha[5]
            infoManuts.append(dictManut)


# Mostra lista de clientes no terminal
def listarClientes(infoClientes):    

    opcao = int(input('[1] Todos os clientes \n[2] Escolher por código: '))

    with open('RegistroSistema/registro_clientes.txt', 'r') as arq:
        for linha in arq:
            linha = linha.rstrip().split(';')
            infoClientes.append(linha)


    # Metodo de ordenação Selection Sort inspirado no codigo mostrado na aula de Algoritmos I
    tam = len(infoClientes)
    for i in range(0, tam-1):
        menor = i
        for j in range(i+1, tam):
            if infoClientes[j] < infoClientes[menor]:
                menor = j
        infoClientes[i], infoClientes[menor] = infoClientes[menor], infoClientes[i]


    # Lista todos
    if opcao == 1:
        os.system('clear')
        print(f'{"Nome": <30}{"Endereço": <30}{"Telefone": <30}{"Código": <30}')
        print('-' * 120)
        for cliente in infoClientes:
            for dado in cliente:
                print(f'{dado: <30}', end='')
            print()

    # Lista por código
    if opcao == 2:
        cod = input('Digite o codigo: ')
        os.system('clear')
        print(f'{"Nome": <30}{"Endereço": <30}{"Telefone": <30}{"Código": <30}')
        print('-' * 120)
        for cliente in infoClientes:
            for dado in cliente:
                if cliente[3] == cod:
                    print(f'{dado: <30}', end='')
    print('\n')

    infoClientes.clear()


# Verifica quantas linhas tem nos arquivos de manutenções para incrementar novo codigo
def criaCodigoManut():

    cont1 = sum(1 for linha in open('RegistroSistema/registro_manut_agenda.txt', 'r'))
    cont2 = sum(1 for linha in open('RegistroSistema/registro_manut_realizada.txt', 'r'))
    return cont1 + cont2


# Agenda nova manutenção (sempre manual)
def agendaManutencao(infoManuts):

    contLinhas = criaCodigoManut()
    codManut = contLinhas + 1

    valor = input('Valor da manutenção: ')
    peça = input('Nome da peça: ').lower()
    id_cliente = input('Código do cliente que receberá manutenção: ')
    data = input('Data de agendamento (DD/MM/AAAA): ')

    if peça in ['filtro de polipropileno','bucha difusora completa']:
        validade = '365'
    elif peça == 'cartucho carvao phb':
        validade = '180'
    else:
        validade = input('Digite a validade da peça em dias, caso não tenha digite 0: ')

    
    manut = [data, valor, peça, validade, id_cliente, codManut]

    with open('RegistroSistema/registro_manut_agenda.txt', 'a') as arq:
        for dados in manut:
            dados = str(dados)
            arq.write(dados + ';')
        arq.write('\n')

    os.system('clear')
    print('Manutenção agendada!\n')
    manut.clear()
    infoManuts.clear()


# Altera ou exclui manutenções com base no código
def editManut(InfoManuts):

    lerArquivoManut()
    opcao = int(input('[1] Editar \n[2] Excluir: '))
    cod = input('Digite o codigo na manutencao: ')


    for manutencao in infoManuts:
        if manutencao['codigo'] == cod:
            if opcao == 1:
                print('Digite o dado que deseja alterar ')
                dado = input('Opções: data, valor, nome da peça, validade, id cliente: ')
                if dado != 'codigo':
                    novodado = input('Digite o novo dado: ').lower()
                    manutencao[dado] = novodado
                    os.system('clear')
                    print('\nDados atualizados.\n')
                else:
                    os.system('clear')
                    print('\nNão é possível alterar o código. \n')

            if opcao == 2:
                infoManuts.remove(manutencao)
                print('Manutenção excluída.')
            
    # Sobrescrevendo alterações no arquivo
    with open('RegistroSistema/registro_manut_agenda.txt', 'w') as arq: 
        for manutencao in infoManuts:
            for dado in manutencao.values():
                arq.write(dado + ';')
            arq.write('\n')   

    infoManuts.clear()


# Realiza manutenção com base no código
def realizarManut(infoManuts):
    lerArquivoManut()
    print(infoManuts)
    cod = input('Digite o codigo da manutenção que deseja concluir: ')
    peça = ''

    for manutencao in infoManuts:    # Inserindo na lista de realizadas
        if manutencao['codigo'] == cod:
            peça = manutencao['peça']
            with open('RegistroSistema/registro_manut_realizada.txt', 'a') as arq:
                for dado in manutencao.values():
                    arq.write(dado + ';')
                arq.write('\n')
            infoManuts.remove(manutencao)

    if infoManuts:
        for manutencao in infoManuts:        # Retirando da lista de agendadas
            with open('RegistroSistema/registro_manut_agenda.txt', 'w') as arq: 
                for dado in manutencao.values():
                    arq.write(dado + ';')
                arq.write('\n')  

    elif not infoManuts:     # Condição necessária para garantir que arquivo será sobrescrito mesmo se lista for vazia
        open('RegistroSistema/registro_manut_agenda.txt', 'w')

    os.system('clear')
    print('Manutenção realizada! ')

    # Verifica se peça tem validade definida
    if peça in ['filtro de polipropileno', 'bucha difusora completa', 'cartucho carvao phb']:
        agendaAutomatico(dictManut, infoManuts)


# Agenda automático apenas após realizar uma manutenção
def agendaAutomatico(dictManut, infoManuts):     
    
    lerArquivoManut()
    contLinhas = criaCodigoManut()

    # Pegando a ultima linha do arquivo de manutençoes realizadas (que acabou de ser alterado)
    with open('RegistroSistema/registro_manut_realizada.txt', 'r') as arq:
        last_line = arq.readlines()[-1]
        last_line = last_line.rstrip().split(';')
        dictManut = {}
        dictManut['data'] = ''
        dictManut['valor'] = last_line[1]
        dictManut['peça'] = last_line[2]
        dictManut['validade'] = last_line[3]
        dictManut['id_cliente'] = last_line[4]
        dictManut['codigo'] = contLinhas + 1 

    # Tratamento de acréscimo de dias de acordo a validade
    validade = int(dictManut['validade'])
    data = date.today() + timedelta(days=validade)
    data = data.strftime("%d/%m/%Y")
    dictManut['data'] = data

    # Inserindo no registro de agendadas
    with open('RegistroSistema/registro_manut_agenda.txt', 'a') as arq:
        for cliente in dictManut.values():
            cliente = str(cliente)
            arq.write(cliente + ';')
        arq.write('\n')

    infoManuts.clear()




# Insere agendadas ou realizadas em matriz para facilitar a ordenação
def listarManut(infoManuts):

    opcao = int(input('[1] Agendadas \n[2] Realizadas: '))
    # Escolha do arquivo correspondente
    if opcao == 1:
        with open('RegistroSistema/registro_manut_agenda.txt', 'r') as arq:
            for linha in arq:
                linha = linha.rstrip().split(';')
                infoManuts.append(linha)
            
    if opcao == 2:
        with open('RegistroSistema/registro_manut_realizada.txt', 'r') as arq:
            for linha in arq:
                linha = linha.rstrip().split(';')
                infoManuts.append(linha)

    # Ordenação
    tam = len(infoManuts)
    for i in range(0, tam-1):
        menor = i
        for j in range(i+1, tam):
            if infoManuts[0][j] < infoManuts[0][menor]:
                menor = j
        infoManuts[0][i], infoManuts[0][menor] = infoManuts[0][menor], infoManuts[0][i]

    os.system('clear')

    # Listagem no console
    print(f'{"Data": <30}{"Valor": <30}{"Peça": <30}{"Validade em dias": <30}{"Id cliente": <30}{"Código": <30}')
    print('-' * 168)
    for manutencao in infoManuts:
        for dado in manutencao:
            print(f'{dado: <30}', end='')
        print()

    save = int(input('\nSalvar em arquivo? \n[1] Sim \n[2] Não: '))  # Salvando em arquivo (sempre sobrescrito)
    if save == 1:
        with open('Manutencoes/ManutencoesAgendadas.csv', 'w', newline='') as arq:
            writer = csv.writer(arq)
            writer.writerow(['Data', 'Valor', 'Peça', 'Validade em dias', 'Id cliente', 'Código'])
            for coluna in infoManuts:
                writer.writerow(coluna)

        os.system('clear')
        print('Relatório salvo!')

    infoManuts.clear()


# Filtra e salva balanço mensal em arquivo csv
def balancoMensal(infoManuts):

    filtro = []

    with open('RegistroSistema/registro_manut_realizada.txt', 'r') as arq:
        for linha in arq:
            linha = linha.rstrip().split(';')
            infoManuts.append(linha)


    opcaoMes = int(input('Deseja consultar qual mês? Insira o mês pelo seu numero correspondente: '))
    opcaoAno = int(input(f'Você escolheu mês {opcaoMes}, digite o ano de consulta: '))

    # Transforma str para date e adiciona na lista referente mês e ano escolhidos
    for i in range(len(infoManuts)):
        data = datetime.strptime(infoManuts[i][0], '%d/%m/%Y').date() 
        if opcaoMes == data.month:
            if opcaoAno == data.year:
                filtro.append(infoManuts[i])

    # Transforma str para float e faz a soma de todos os valores
    soma = 0
    for i in range(len(filtro)):
        valor = float(filtro[i][1])
        soma += valor

    os.system('clear')

    # Verifica se houveram manutenções no período escolhido
    if filtro:
        print(f'{"Data": <30}{"Valor": <30}{"Peça": <30}{"Validade em dias": <30}{"Id cliente": <30}{"Código": <30}')
        print('-' * 168)
        for manutencao in filtro:
            for dado in manutencao:
                print(f'{dado: <30}', end='')
            print()
        print(f'{"VALOR TOTAL": <30}', soma)

        save = int(input('\nSalvar em arquivo? \n[1] Sim \n[2] Não: '))
        if save == 1:
            with open('BalancoMensal/BalancoMensal.csv', 'w', newline='') as arq:
                writer = csv.writer(arq)
                writer.writerow(['Data', 'Valor', 'Peça', 'Validade em dias', 'Id cliente', 'Código'])
                for coluna in filtro:
                    writer.writerow(coluna)
                writer.writerow(['Total', soma])
            os.system('clear')
            print('Relatório salvo!')

     # Informa ao usuário se não existir manutenções no período escolhido
    if not filtro:
        print('Não existem manutenções do mês e ano escolhidos.')

    infoManuts.clear()


# Programa principal 

# Essas estruturas são sempre recicladas para que possam ser usadas em várias funções
# Seu conteúdo é frequentemente apagado e novos dados são inseridos
dictCliente = {}
infoClientes = []
dictManut = {}
infoManuts = []

menuPrincipal()
