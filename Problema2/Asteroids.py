'''*******************************************************************************
Autor: Letícia Teixeira Ribeiro dos Santos
Componente Curricular: Algoritmos I
Concluido em: 25/04/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************'''

from os import system
from time import sleep
import keyboard
from random import randint


def mostra_matriz():
  for linha in matriz:
    for coluna in linha:
      print(coluna,end='')
    print()

# Movimentação 
# O break foi utilizado nas funções a seguir por que era necessário percorrer a matriz apenas até certo ponto
def direita():

  system('cls')
  
  for i in range(0,36):
    if matriz[23][i] == '*':
      matriz[23][i] = ' '
      matriz[23][i+1] = '*'
      break

  for j in range(0,36):
    if matriz[24][j] == '*':
      matriz[24][j] = ' '
      matriz[24][j+3] = '*'
      break

  mostra_matriz()


def esquerda():

  system('cls')

  for i in range(0,36):
    if matriz[23][i] == '*':
      matriz[23][i] = ' '
      matriz[23][i-1] = '*'
      break

  for j in range(36,0,-1):
    if matriz[24][j] == '*':
      matriz[24][j] = ' '
      matriz[24][j-3] = '*'
      break

  mostra_matriz()
  

# Verificando posição atual da nave para atirar o projétil
def projetil():

  system('cls')

  for j in range(0,35):
    if matriz[23][j] == '*':
      matriz[22][j] = 'o'
      break


# Movendo o projetil na tela uma coluna a menos a cada chamada
def move_projetil():

  for i in range(0,23):
    for j in range(1,36):
      if matriz[i][j] == 'o' and i >= 2:
        matriz[i][j] = ' '
        matriz[i-1][j] = 'o'

      # Essa condiçao foi criada pro projetil sumir da tela apenas apos atingir o topo
      if matriz[i][j] == 'o' and i < 2:
        matriz[i][j] = ' '


# Movendo asteroide uma coluna a mais a cada chamada
def move_asteroide(posicao, num):

  # Limpando posiçao anterior do asteroide
  for i in range(1,23):
    for j in range(1,36):
      if matriz[i][j] == '*':
        matriz[i][j] = ' '

  # Definindo o asteroide
  for i in range(3):
    matriz[num][posicao+i] = '*'
    matriz[num+4][posicao+i] = '*'
  
  for i in range(-1, 4):
    matriz[num+1][posicao+i] = '*'
    matriz[num+3][posicao+i] = '*'

  for i in range(-2, 5):
    matriz[num+2][posicao+i] = '*'

  # Resetando temporizador de descida do asteroide para proxima iteração do while
  timer = 0

  return timer


def colisoes(num, posicao, vidas, esc, pontuacao):

    # Essa condição verifica se houve colisão entre nave e asteroide
  if num == 19:
    if matriz[23][posicao] == '*' or matriz[23][posicao+1] == '*' or matriz[23][posicao+2] == '*':
      print('O asteroide colidiu com a nave!!! GAME OVER.')
      esc = True
      vidas = 0

  # Essa condição se torna verdadeira quando o asteroide chega proximo ao fim do cenário sem ser destruído
  if matriz[22][posicao] == '*':
    sleep(1)
    vidas-=1
    for i in range(1,23):
      for j in range(1,36):
        if matriz[i][j] == 'o' or matriz[i][j] == '*':  # Reiniciando o cenário
          matriz[i][j] = ' '
    num = 1
    posicao = randint(3,31)

  # Essa repetição verifica se houve colisão do tiro e asteroide a cada iteração do while
  for i in range(0,23):
    for j in range(1,36):
      if matriz[i][j] == 'o' and matriz[i-1][j] == '*':
        pontuacao += 10
        matriz[i][j] = ' '
        num = 1
        posicao = randint(3,31)

  return num, vidas, posicao, pontuacao


def jogo():

  # Posicao inicial da nave a cada novo jogo
  matriz[23][17] = '*'
  matriz[24][16] = '*'
  matriz[24][17] = '*'
  matriz[24][18] = '*'

  pontuacao = 0    
  posicao = randint(3,31)  # Intervalo de randomização escolhido para asteroide caber em até 5 colunas
  tiro = False  # Essa variavel muda de valor quando o primeiro projetil é disparado
  esc = False  # Essa variável muda de valor quando o jogador deseja sair do jogo
  num = 1   # Essa variável controla a descida do asteroide
  timer = 0
  vidas = 10


  while vidas > 0 and esc == False:

    system('cls')

    timer+=1

     # Essa condição controla a quantidade de vezes que o asteroide se move
    if timer == 6:
      timer = move_asteroide(posicao, num)
      num+=1

    mostra_matriz() 

    print('Pontuação: ', pontuacao)
    print('Vidas: ', vidas)

    if keyboard.is_pressed('left'):
      esquerda()

    if keyboard.is_pressed('right'):
      direita()

    if keyboard.is_pressed('space'):
      projetil()
      tiro = True  

    # Essa condição controla a chamada da função move_projetil
    if tiro:
      move_projetil()

    if keyboard.is_pressed('esc'):
      esc = True
      vidas = 0

    # Nessa função foi necessário pegar os valores como parametro e também retorná-los
    # para que as outras funções saibam da mudança de valores ocorrida
    num, vidas, posicao, pontuacao = colisoes(num, posicao, vidas, esc, pontuacao)

    sleep(0.04)

  return num, posicao, vidas, pontuacao

def menu():

  cont = 0

  print('''
         ___         __                  _     __    
        /   |  _____/ /____  _________  (_)___/ /____
       / /| | / ___/ __/ _ \/ ___/ __ \/ / __  / ___/
      / ___ |(__  ) /_/  __/ /  / /_/ / / /_/ (__  ) 
     /_/  |_/____/\__/\___/_/   \____/_/\__,_/____/ ''')

  print('\n')

  print('''           INSTRUÇOES:
          > Utilize as teclas de seta direita e esquerda para movimentar a nave
          > Aperte a tecla space para atirar no asteroide
          > Movimente a nave dentro do limite do cenário para evitar erros na jogabilidade
          > Se um asteroide colidir na nave, você morre :(
          > Você perde uma vida a cada asteroide que não destrói.

                    LET'S GO!''')

  jogador = ()
  recordes = []

  while cont == 0:

    escolha = int(input('\n[1] Jogar \n[2] Recordes \n[3] Sobre \n[4] Sair: '))


    if escolha == 1:
    
      # Limpando o cenário caso o jogador saia e depois queira voltar a jogar na mesma execução
      for i in range(1,25):
        for j in range(1,36):
          if matriz[i][j] == '*' or matriz[i][j] == 'o':
            matriz[i][j] = ' '

      sleep(1)
      num, posicao, vidas, pontuacao = jogo()

      jogador = pontuacao, input('Seu nome: ' )

      # Pontuações são adicionadas sem critério até chegar ao top 4 
      if len(recordes) <= 4:
        recordes.append(jogador)

      # Ao chegar a 5 as pontuações seguintes passam por um filtro
      else:
        recordes = sorted(recordes)
        if recordes[0][0] < jogador[0]:
          recordes.pop(0)
          recordes.append(jogador)

      recordes_finais = sorted(recordes, reverse=True)

    elif escolha == 2:
      print()
      if len(recordes) == 0:
        print('Ainda não há recordes!!')
      else:
        for elemento in recordes_finais:
          print(elemento)

    elif escolha == 3:
      print()
      print('Projeto inspirado no jogo de tiro lançado na década de 70: Asteroids!')
      print('----------------------------------------------------------------------')
      print('Developed by Leticia Ribeiro')
        

    elif escolha == 4:
      print('Você saiu do jogo.')
      sleep(1)
      cont = 1

    elif escolha < 1 or escolha > 4:
      print()
      print('Opção inválida!!')
    


# Programa principal
# Criação da matriz com cenário
matriz = []

for i in range(26):
  linha = []
  for j in range(37):
    if j == 0 or j == 36:
      linha.append('█')
    else:
      linha.append(' ')
  matriz.append(linha)


for j in range(37):
  matriz[0][j] = '▄'
  matriz[25][j] = '▀'

menu()