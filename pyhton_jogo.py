print('Seja bem vindo ao jogo da velha')
print('Começamos com o X')
tabuleiro = [1, 2, 3, 4, 5, 6, 7, 8, 9]
isP1 = True
def r():
  if tabuleiro[0] == tabuleiro[1] == tabuleiro[2]:
    print(f"Jogador {tabuleiro[0]} ganhou")
    return True
  elif tabuleiro[0] == tabuleiro[4] == tabuleiro[8]:
    print(f'Jogador {tabuleiro[0]}  ganhou')
    return True
  elif tabuleiro[0] == tabuleiro[3] == tabuleiro[6]:
    print(f'Jogador {tabuleiro[0]}  ganhou')
    return True
  elif tabuleiro[1] == tabuleiro[4] == tabuleiro[7]:
    print(f"Jogador  {tabuleiro[1]}  ganhou")
    return True
  elif tabuleiro[2] == tabuleiro[5] == tabuleiro[8]:
    print(f'Jogador  {tabuleiro[2]}  ganhou')
    return True
  elif tabuleiro[2] == tabuleiro[4] == tabuleiro[5]:
    print(f'Jogador  {tabuleiro[2]}  ganhou')
    return True
  elif tabuleiro[6] == tabuleiro[7] == tabuleiro[8]:
    print(f'Jogador {tabuleiro[6]}  ganhou')
    return True
  elif tabuleiro[2] == tabuleiro[4] == tabuleiro[6]:
    print(f'Jogador  {tabuleiro[2]}  ganhou')
    return True
  else:
    return False
# TABELA JOGO
def JogoDaVelha():
  print('', tabuleiro[0], "   |   ", tabuleiro[1], "   |   ", tabuleiro[2])
  print("---   |   ---   |   ---\n")
  print('', tabuleiro[3], "   |   ", tabuleiro[4], "   |   ", tabuleiro[5])
  print("---   |   ---   |   ---\n")
  print('', tabuleiro[6], "   |   ", tabuleiro[7], "   |   ", tabuleiro[8])
def main():
  while True:
    JogoDaVelha()
    global isP1
    isP1 = not isP1
    p = int(input("digite: "))
    if tabuleiro[p-1] == "x" or tabuleiro[p-1] == "o":
      print("queridao essa ja foi!! --, perdeu a vez")
      continue
    if p <1 or p > 9:
      print("Esta posição não foi encontrada, perdeu a vez")
      continue
    tabuleiro[p-1] = "\033[1;31;40m x \033[m" if isP1 else "\033[1;36;40m o \033[m"
    if(r()):
        break
main()
