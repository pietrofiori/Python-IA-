import random

# Criando o tabuleiro
T = [[0,0,0],[0,0,0],[0,0,0]]

# Função para imprimir o tabuleiro
def imprimir_tabuleiro():
    for i in range(3):
        for j in range(3):
            print(T[i][j], end=' ')
        print()

# Função para verificar se alguém ganhou
def verificar_ganhador(jogador):
    # Verificando linhas
    for i in range(3):
        if T[i][0] == T[i][1] == T[i][2] == jogador:
            return True
    # Verificando colunas
    for j in range(3):
        if T[0][j] == T[1][j] == T[2][j] == jogador:
            return True
    # Verificando diagonais
    if T[0][0] == T[1][1] == T[2][2] == jogador:
        return True
    if T[0][2] == T[1][1] == T[2][0] == jogador:
        return True
    # Caso ninguém tenha ganhado ainda
    return False

# Função para jogar
def jogar(jogador):
    if jogador == 'X':
        # Sua jogada
        print("-----------")
        print("Sua jogada (jogador X)")
        i, j = map(int, input("Digite a linha e a coluna (separadas por espaço): ").split())
        while T[i][j] != 0:
            print("Posição ocupada, tente novamente")
            i, j = map(int, input("Digite a linha e a coluna (separadas por espaço): ").split())
        T[i][j] = 'X'
    else:
        # Jogada do computador (jogador 2)
        print("-----------")
        print("Jogada do computador (jogador O)")
        i, j = random.choice([(i,j) for i in range(3) for j in range(3) if T[i][j] == 0])
        T[i][j] = 'O'
    imprimir_tabuleiro()
    return verificar_ganhador(jogador)

# Jogando até que alguém ganhe ou não haja mais posições livres
jogador_atual = 'O'
while True:
    if jogar(jogador_atual):
        print("Jogador", jogador_atual, "venceu!")
        break
    jogador_atual = 'O' if jogador_atual == 'X' else 'X'
    # Verificando se há posições livres no tabuleiro
    if all(all(row) for row in T):
        print("Não há mais posições livres!")
        break

jogar(jogador='X')