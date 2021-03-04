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


print("Vacinação em X")



#listas para armazenar dados necessários

nomes = []
cpf = []
sexo = []
prioridade = []
localVacinacao = []
dia = []
horario = []   #foi necessario duas listas de horario pois uma pegará do usuário o horário como string
horarioFormatado = []     #e a outra será a transformação desses dados em inteiros
tipoVacina = []
doseVacina = []
contador = [0]*5
loteVacina = []
i = 0  #quantidade de vacinados


#cada indice da lista "contador" será um tipo de contador
#contador[0] = vacinadas do sexo feminino
#contador[1] = vacinados pela manhã
#contador[2] = tipo vacina 
#contador[3] = primeira dose
#contador[] = idosos vacinados


def relatorioParcial(i):
    print('Quantidade de vacinados: ', i)
    print('Quantidade de primeiras doses aplicadas: ', contador[3])
    print('Quantidade de segundas doses aplicadas: ', i - contador[3]) #subtraindo primeiras doses da quantidade total de vacinados
    print('Percentual de vacinados com Coronavac: ', (contador[2]*100) / i)
    print('Percentual de vacinados com AstraZeneca', (100) - (contador[2]*100) / i)
    print('Percentual de vacinas aplicadas pela manhã: ', (contador[1]*100) / i)
    print('Percentual de vacinados do sexo feminino: ', (contador[0]*100) / i)
    print('Percentual de vacinados do sexo masculino: ', (100) - (contador[0]*100))

def menu(i):

    while True:

        escolha = int(input('[1] Cadastrar novo paciente \n[2] Visualizar Relatório Parcial \n[3] Sair --> '))

        if escolha == 2:
            relatorioParcial(i)
            
            
        if escolha == 3: 
            break

        nomes.append(input('Nome: '))
        cpf.append(input('CPF: '))
        sexo.append(int(input('[1] Feminino \n[2] Masculino: ')))
        if sexo[i] == 1:
            contador[0] += 1

        localVacinacao.append(input('Local da vacinação: '))
        dia.append(input('Dia da vacinação (Ex: DD/MM/AAAA): '))
        horario.append(input('Horario da vacinação (Ex: 8:00, 9:25): '))
        horario[i] = horario[i].replace(':', '')
        horarioFormatado.append(int(i))   #transformando horarios em int e transferindo para outra lista
        if horarioFormatado[i] >= 800 and horarioFormatado[i] <=1259:  #verificando se foi período manhã
            contador[1] += 1

        tipoVacina.append(int(input('[1] Coronavac \n[2] Astrazeneca: ')))
        if tipoVacina[i] == 1:
            contador[2] += 1

        doseVacina.append(int(input('[1] Primeira dose \n[2] Segunda dose: ')))
        if doseVacina[i] == 1:
            contador[3] += 1

        loteVacina.append(input('Lote da vacina: '))
        
        i += 1


menu(i)