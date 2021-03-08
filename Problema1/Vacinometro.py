'''*******************************************************************************
Autor: Letícia Teixeira Ribeiro dos Santos
Componente Curricular: Algoritmos I
Concluido em: 
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************'''


print('Vacinação em X\n')
print('O que deseja fazer?\n')




#essas variaveis serão utilizadas como contadores dentro das funções
doseUm = 0
sexoFeminino = 0
periodoManha = 0
totalDeDoses = 0
coronavac = 0




def relatorioParcial(totalDeDoses):   #variavel contadora foi passada como parametro nas duas funções

    print('Quantidade de vacinados: ', doseUm)  #se considera o total de vacinados a partir da contagem das primeiras doses
    print('Quantidade de doses aplicadas: ', totalDeDoses)
    print('Quantidade de pessoas que receberam a primeira dose: ', doseUm)
    print('Quantidade de pessoas que receberam a segunda dose: ', totalDeDoses - doseUm) #subtraindo total de doses das primeiras para descobrir o total de segundas doses
    print('Percentual de vacinados com Coronavac: ', (coronavac*100) / totalDeDoses)
    print('Percentual de vacinados com AstraZeneca', (100) - (coronavac*100) / totalDeDoses) #foi pego o percentual da coronavac e substraido por 100 para obter o percentual da astrazeneca
    print('Percentual de vacinas aplicadas pela manhã: ', (periodoManha*100) / totalDeDoses)       
    print('Percentual de vacinados do sexo feminino: ', (sexoFeminino*100) / totalDeDoses)
    print('Percentual de vacinados do sexo masculino: ', (100) - (sexoFeminino*100) / totalDeDoses)

def menu(totalDeDoses):

    while True:

        escolha = int(input('[1] Cadastrar novo paciente \n[2] Visualizar Relatório Parcial \n[3] Sair --> '))

        if escolha == 2:
            try:
                relatorioParcial(totalDeDoses)
            except ZeroDivisionError:  #tratamento de erro caso o usuario queira ver relatorio antes de cadastrar alguem
                print('Erro ao obter percentuais! Ainda não há pessoas cadastradas. ')  ##complementar!
                
            
        if escolha == 3: 
            print('Programa finalizado.')
            break

        if escolha < 1 or escolha > 3:
            print('Digite uma opção valida!! ') #tratamento de erro caso usuario escolha opção inexistente
            continue

        nome = input('Nome completo: ')
        cpf = input('CPF: ')
        doseVacina = int(input('[1] Primeira dose \n[2] Segunda dose: '))
        if doseVacina == 1:
            global doseUm  #informando para o programa alterar a variavel global, não criar uma nova
            doseUm += 1   #somando nesta variavel caso atenda a condição do if

        loteVacina = input('Lote da vacina: ')
        localVacinacao = input('Local da vacinação: ')

        sexo = int(input('[1] Feminino \n[2] Masculino: '))
        if sexo == 1:
            global sexoFeminino
            sexoFeminino += 1

        dia = input('Dia da vacinação (Ex: DD/MM/AAAA): ')
        horario = input('Horario da vacinação de 8:00 às 18:00 (Ex: 8:25, 15:00) ') #pegando horario como string
        horario = horario.replace(':', '') #retirando o ":" para manipular variavel como tipo inteiro
        horarioFormatado = int(horario)   #transformando horario em int e transferindo para outra variavel
        if horarioFormatado >= 800 and horarioFormatado <=1259: #verificando se foi periodo manhã (entre 8:00 às 12:59)
            global periodoManha
            periodoManha += 1

        tipoVacina = int(input('[1] Coronavac \n[2] Astrazeneca: '))
        if tipoVacina == 1:
            global coronavac
            coronavac += 1
        
        totalDeDoses += 1

#programa inicia chamando a função menu
menu(totalDeDoses)