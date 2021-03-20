'''*******************************************************************************
Autor: Letícia Teixeira Ribeiro dos Santos
Componente Curricular: Algoritmos I
Concluido em: 12/03/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************'''



#Variaveis contadoras que serão utilizadas nos cálculos.
doseUm = 0
sexoFeminino = 0
periodoManha = 0
totalDeDoses = 0
coronavac = 0
qtdIdosos = 0



def relatorioParcial(totalDeDoses):   
    
    '''dependendo do que se pede em cada requisito, alguns valores foram 
    divididos pelo total de vacinados, e outros pelo total de doses'''
    percentCoronavac = (coronavac*100) / doseUm
    percentAstrazeneca = (100) - (coronavac*100) / doseUm
    percentIdosos = (qtdIdosos*100) / doseUm
    percentManha = (periodoManha*100) / totalDeDoses
    percentTarde = (100) - (periodoManha*100) / totalDeDoses   
    percentFeminino = (sexoFeminino*100) / doseUm
    percentMasculino = (100) - (sexoFeminino*100) / doseUm

    #Se considera o total de vacinados a partir da contagem das primeiras doses.
    print('Quantidade de vacinados: ', doseUm)  
    print('Quantidade de doses aplicadas: ', totalDeDoses)
    print('Quantidade de pessoas que receberam a primeira dose: ', doseUm)
    print('Quantidade de pessoas que receberam a segunda dose: ', totalDeDoses - doseUm)
    
    #Foi utilizado print formatado apenas em percentuais para limitar número de casas decimais.
    print(f'Percentual de vacinados com Coronavac: {percentCoronavac:.1f}%')  
    print(f'Percentual de vacinados com AstraZeneca: {percentAstrazeneca:.1f}%')
    print(f'Percentual de idosos vacinados: {percentIdosos:.1f}%')
    print(f'Percentual de vacinas aplicadas pela manhã: {percentManha:.1f}%')
    print(f'Percentual de vacinas aplicadas pela tarde: {percentTarde:.1f}%')    
    print(f'Percentual de vacinados do sexo feminino: {percentFeminino:.1f}%')
    print(f'Percentual de vacinados do sexo masculino: {percentMasculino:.1f}%')


print('*'*15)
print('  VACINÔMETRO')
print('*'*15)
print('O que deseja fazer? Escolha por número:\n')


def menu(totalDeDoses):
    
    iterador = 0

    while iterador == 0:

        escolha = int(input('[1] Cadastrar Pessoa \n[2] Visualizar Relatório Parcial \n[3] Sair --> '))
        
        if escolha == 1:
            nome = input('Nome completo: ')  
            cpf = input('CPF: ')
            dia = input('Dia da vacinação (Ex: DD/MM/AAAA): ')

            #Para contabilizar como período manhã
            #os horários foram pedidos como string, foi retirado caractere indesejado
            #transformado em inteiro e comparado na condição.
            horario = input('Horario da vacinação de 8:00 às 18:00 (Ex: 8:25, 15:00): ')
            horario = horario.replace(':', '') 
            horarioFormatado = int(horario)    
            if horarioFormatado >= 800 and horarioFormatado <=1159:
                #Contabilizando na variável global existente.
                global periodoManha
                periodoManha += 1 
        
            loteVacina = input('Lote da vacina: ')

            doseVacina = int(input('[1] Primeira dose \n[2] Segunda dose: '))
            if doseVacina == 1:
                global doseUm  
                doseUm += 1

            #Essa condição apenas contabiliza caso seja a segunda dose e interrompe a entrada de dados
            if doseVacina == 2:
                totalDeDoses += 1
                print('Segunda dose contabilizada!\n')
                continue

            #se for segunda dose não será necessário pegar os dados abaixo novamente
            sexo = int(input('[1] Feminino \n[2] Masculino: '))
            if sexo == 1:
                global sexoFeminino
                sexoFeminino += 1

            tipoVacina = int(input('[1] Coronavac \n[2] Astrazeneca: '))
            if tipoVacina == 1:
                global coronavac
                coronavac += 1

            prioridade = input('Digite o grupo prioritário do vacinado: ')
        
            idoso = int(input('Idade a partir de 60 anos? \n[1] Sim \n[2] Não: '))
            if idoso == 1:
                global qtdIdosos
                qtdIdosos += 1

            localVacinacao = input('Local da vacinação: ')
            print(nome, 'foi cadastrado com sucesso.\n')

            totalDeDoses += 1


        elif escolha == 2:
            #Tratamento de erro caso o usuário queira ver relatorio antes de cadastrar alguém
            try:
                relatorioParcial(totalDeDoses)
                continue
            except ZeroDivisionError:
                print('Erro ao obter percentuais! Ainda não há pessoas cadastradas. ')
                continue


        #programa é encerrado caso variável de controle do loop mude de valor
        elif escolha == 3:
            iterador = 1 
            print('Programa finalizado.')
        

        #Tratamento de erro caso usuário escolha opção inexistente.
        elif escolha < 1 or escolha > 3:
            print('Digite uma opção valida!! ')
            continue

#programa inicia chamando a função menu
menu(totalDeDoses)