from os import system
from time import sleep
import keyboard
from random import randint

matriz = [
  [' ','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',' '],
  ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
  ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
  ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
  ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
  ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
  ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
  ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
  ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
  ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
  ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
  ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
  ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
  ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
  ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
  ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
  ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
  ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
  ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
  ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
  ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
  ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
  ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
  ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
  ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
  ['|','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','|']
]
#0a 36 lin = 37 linhas. 2 pro cenario
#0 a 25 col
#0 e 25 é cenario

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

  mostra_matriz()  #chamando essa funçao dnv pq se nao chamar o mapa do jogo demora mais pra printar dnv

def esquerda():

  system('cls')

  for k in range(0,36):
    if matriz[23][k] == '*':
      matriz[23][k] = ' '
      matriz[23][k-1] = '*'
      break

  for m in range(36,0,-1):
    if matriz[24][m] == '*':
      matriz[24][m] = ' '
      matriz[24][m-3] = '*'
      break

  mostra_matriz()
  
# Verificando posição da nave atual para atirar o projetil
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
      if matriz[i][j] == 'o' and i < 2:  #essa condiçao foi criada pro projetil sumir na tela apenas apos atingir o topo
        matriz[i][j] = ' '

# Movendo asteroide uma coluna a mais a cada chamada
def move_asteroide(posicao, n):

  # Limpando posiçao anterior do asteroide
  for i in range(1,22):
    for j in range(1,36):
      if matriz[i][j] == '*':
        matriz[i][j] = ' '

  matriz[n][posicao] = '*'
  matriz[n][posicao+1] = '*'
  matriz[n][posicao+2] = '*'

  matriz[n+1][posicao-1] = '*'
  matriz[n+1][posicao] = '*'
  matriz[n+1][posicao+1] = '*'
  matriz[n+1][posicao+2] = '*'
  matriz[n+1][posicao+3] = '*'

  matriz[n+2][posicao-2] = '*'
  matriz[n+2][posicao-1] = '*'
  matriz[n+2][posicao] = '*'
  matriz[n+2][posicao+1] = '*'
  matriz[n+2][posicao+2] = '*'
  matriz[n+2][posicao+3] = '*'
  matriz[n+2][posicao+4] = '*'

  matriz[n+3][posicao-1] = '*'
  matriz[n+3][posicao] = '*'
  matriz[n+3][posicao+1] = '*'
  matriz[n+3][posicao+2] = '*'
  matriz[n+3][posicao+3] = '*'

  matriz[n+4][posicao] = '*'
  matriz[n+4][posicao+1] = '*'
  matriz[n+4][posicao+2] = '*'

  x = 0  #resetando variavel pra contar dnv no while

  return n, x


def jogo():

  # Posicao inicial da nave a cada novo jogo
  matriz[23][17] = '*'
  matriz[24][16] = '*'
  matriz[24][17] = '*'
  matriz[24][18] = '*'

  pontuacao = 0    
  posicao = randint(3,31)
  a = False
  n = 1
  x = 0
  vidas = 10
  esc = False

  print('''                       INSTRUÇOES:
      - Utilize as teclas de seta direita e esquerda para movimentar a nave
      - Movimente a nave dentro do limite do cenário para evitar erros na jogabilidade''')

  sleep(10)

  while vidas > 0 and esc == False:

    system('cls')

    print('Pontuação: ', pontuacao)
    print('Vidas: ', vidas)
    

    x+=1

     # Essa condição controla a quantidade de vezes que o asteroide se move
    if x == 8:
      n, x = move_asteroide(posicao, n)
      n+=1

    mostra_matriz() 

    if keyboard.is_pressed("left"):
      esquerda()

    if keyboard.is_pressed("right"):
      direita()

    if keyboard.is_pressed('space'):
      projetil()
      # Essa variavel muda de valor quando o primeiro projetil é disparado
      a = True  

    # Essa condição controla a chamada da função move_projetil
    if a:
      move_projetil()

    if keyboard.is_pressed('esc'):
      esc = True
      vidas = 0


    # Essa condição se torna verdadeira quando o asteroide chega proximo ao fim do cenário sem ser destruído
    if matriz[22][posicao] == '*':
      sleep(1)
      vidas-=1
      for i in range(0,23):
        for j in range(1,36):
          if matriz[i][j] == 'o' or matriz[i][j] == '*':  #limpando asteroide e tiros da tela
            matriz[i][j] = ' '
          n = 1
          posicao = randint(3,31)

    # Essa repetição verifica se houve colisão do tiro e asteroide a cada iteração do while
    for i in range(0,23):
      for j in range(1,36):
        if matriz[i][j] == 'o' and matriz[i-1][j] == '*':
          sleep(1)
          pontuacao += 10
          matriz[i][j] = ' '
          n = 1
          posicao = randint(3,31)

    sleep(0.06)

  return n, x, posicao, vidas, pontuacao

def main():

  cont = 0

  print('''
         ___         __                  _     __    
        /   |  _____/ /____  _________  (_)___/ /____
       / /| | / ___/ __/ _ \/ ___/ __ \/ / __  / ___/
      / ___ |(__  ) /_/  __/ /  / /_/ / / /_/ (__  ) 
     /_/  |_/____/\__/\___/_/   \____/_/\__,_/____/ ''')

  print('\n')

  jogador = ()
  recordes = []

  while cont == 0:

    escolha = int(input('\n[1] Jogar \n[2] Recordes \n[3] Sobre \n[4] Sair: '))


    if escolha == 1:
      # Limpando toda a matriz se for o caso do jogador apertar "esc" e depois querer voltar a jogar
      for i in range(0,23):
        for j in range(1,36):
          if matriz[i][j] == '*' or matriz[i][j] == 'o':
            matriz[i][j] = ' '

      sleep(1)
      n, x, posicao, vidas, pontuacao = jogo()

      jogador = pontuacao, input('Seu nome:' )
      # Pontuações são adicionadas sem critério até chegar ao top 4 
      if len(recordes) <= 4:
        recordes.append(jogador)
 
      else:
        recordes = sorted(recordes)
        if recordes[0][0] < jogador[0]:
          recordes.pop(0)
          recordes.append(jogador)

      recordes_finais = sorted(recordes, reverse=True)

    if escolha == 2: 

      for elemento in recordes_finais:
        print(elemento)

    if escolha == 3:
      
      print('''Projeto inspirado no jogo de tiro lançado em 1978: Space Invaders
        Desenvolvido por Letícia Ribeiro em 2021.''' )

    if escolha == 4:
      print('Você saiu do jogo.')
      cont = 1

main()