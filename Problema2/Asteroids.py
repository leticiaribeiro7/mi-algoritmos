import os
import time
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

#colocar em main
print('***********ASTEROIDS*********')

def mostra_nave():
  for linha in matriz:
    for coluna in linha:
      print(coluna,end='')
    print()

#a cada if de derrota da rodada vai ser chamada mostra asteroide dnv para aleatorizar o asteroide


def direita():

  os.system('cls')
  
  for j in range(0,36):
    if matriz[23][j] == '*':
      matriz[23][j] = ' '
      matriz[23][j+1] = '*'
      break

  for l in range(0,36):
    if matriz[24][l] == '*':
      matriz[24][l] = ' '
      matriz[24][l+3] = '*'
      break

  mostra_nave()

def esquerda():

  os.system('cls')

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


  mostra_nave()
    
def projetil():

  os.system('cls')

  for j in range(0,32):
    if matriz[23][j] == '*':
      matriz[22][j] = 'o'
      break

  mostra_nave()

def move_projetil():

  for i in range(0,23):
    for j in range(1,36):
      if matriz[i][j] == 'o' and i >= 2:
        matriz[i][j] = ' '
        matriz[i-1][j] = 'o'
      if matriz[i][j] == 'o' and i < 2:  #essa condiçao foi criada pro projetil sumir na tela apenas apos atingir o topo
        matriz[i][j] = ' '


def move_asteroide(posicao, n):

  #limpando posiçao anterior do asteroide
  for i in range(1,22):
    for j in range(0,34):
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

  pontuacao = 0
  posicao = randint(3,31)     #vai ser chamado dnv a cada vida perdida ou aumento de pont
  a = False
  n = 1
  x = 0   #essas var mudam de valor dentro da funçao jogo
  vidas = 10

  while vidas > 0:

    os.system('cls')

    print('Vidas:', vidas)
    print('Pontuação: ', pontuacao) #de acordo a projetil atingindo asteroide
    
    x+=1

    if x == 2:
      n, x = move_asteroide(posicao, n)
      n+=1

    mostra_nave() 

    if keyboard.is_pressed("left"):
      esquerda()

    if keyboard.is_pressed("right"):
      direita()

    if keyboard.is_pressed('space'):
      projetil()
      a = True         # variavel 'a' muda de valor quando o primeiro projetil é disparado

    if a:     # movendo projeteis pro topo da tela a cada iteração
      move_projetil()

    if keyboard.is_pressed('esc'):
      break

    # movendo projeteis pro topo da tela a cada iteração

    #se asteroide chegar proximo do final do cenario sem ser destruido, tbm serve pra colisao da nave e asteroide
    if matriz[22][posicao] == '*':
      time.sleep(1)
      vidas-=1
      for i in range(0,23):
        for j in range(1,36):
          if matriz[i][j] == 'o' or matriz[i][j] == '*':  #limpando asteroide e tiros da tela
            matriz[i][j] = ' '
          n = 1
          posicao = randint(3,31)

    for i in range(0,23):
      for j in range(1,36):
        if matriz[i][j] == 'o' and matriz[i-1][j] == '*':
          pontuacao += 10
          time.sleep(1)
          matriz[i][j] = ' '
          n = 1
          posicao = randint(3,31)

    time.sleep(0.08)

  return n, x, posicao, vidas, pontuacao

#talvez botar dentro de main
i = 0
recordes = {}

while i == 0:

  escolha = int(input('[1] Jogar \n[2] Recordes \n[3] Sobre \n[4] Sair: '))


  if escolha == 1:
    #posiçao inicial da nave a cada novo jogo
    matriz[23][17] = '*'
    matriz[24][16] = '*'
    matriz[24][17] = '*'
    matriz[24][18] = '*'
    time.sleep(1)
    n, x, posicao, vidas, pontuacao = jogo()

    nome = input('Digite seu primeiro nome: ')
    recordes[nome] = pontuacao


  if escolha == 2:   #ver forma mais bonita de printar o dict
    print('Recordes: ', recordes)

  if escolha == 3:
    #ver oq botar aqui na sessao

  if escolha == 4:
    print('Você saiu do jogo.')
    i = 1
