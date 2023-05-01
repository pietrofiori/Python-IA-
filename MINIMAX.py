import random

T = [[0,0,0],[0,0,0],[0,0,0]]


def imprimir_tabuleiro():
    for i in range(3):
        for j in range(3):
            if T[i][j] == 'X':
                print(Fore.RED + "X" + Style.RESET_ALL, end=" ")
            elif T[i][j] == 'O':
                print(Fore.BLUE + "O" + Style.RESET_ALL, end=" ")
            else:
                print("0", end=" ")
        print()

# função para verificar se alguém ganhou
def verificar_ganhador(jogador):
    #  linhas
    for i in range(3):
        if T[i][0] == T[i][1] == T[i][2] == jogador:
            return True
    #  colunas
    for j in range(3):
        if T[0][j] == T[1][j] == T[2][j] == jogador:
            return True
    #  diagonais
    if T[0][0] == T[1][1] == T[2][2] == jogador:
        return True
    if T[0][2] == T[1][1] == T[2][0] == jogador:
        return True
    # se ninguém tenha ganhado ainda
    return False

def minimax(tabuleiro, jogador, profundidade):
    # Verifica se o estado atual é terminal
    resultado = verificar_ganhador(jogador)
    if resultado != 0:
        return resultado

    # Se ainda não há um resultado, faz a busca recursiva
    if jogador == 'X':
        melhor_valor = -float('inf')
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == 0:
                    tabuleiro[i][j] = jogador
                    valor = minimax(tabuleiro, 'O', profundidade+1)
                    tabuleiro[i][j] = 0
                    melhor_valor = max(melhor_valor, valor)
        return melhor_valor
    else:
        melhor_valor = float('inf')
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == 0:
                    tabuleiro[i][j] = jogador
                    valor = minimax(tabuleiro, 'X', profundidade+1)
                    tabuleiro[i][j] = 0
                    melhor_valor = min(melhor_valor, valor)
        return melhor_valor

# achei interessante colocar cores no X e O para facilitar a visualização 
from colorama import init, Fore, Style
init() 

def jogar(jogador):
    if jogador == 'X':
        # sua jogada (jogador 1)
        print("Sua jogada (jogador X)")
        i, j = map(int, input("Digite a linha e a coluna (separadas por espaço): ").split())
        while T[i][j] != 0:
            print("Posição ocupada, tente novamente")
            i, j = map(int, input("Digite a linha e a coluna (separadas por espaço): ").split())
        if i == 0:
            print(Fore.RED + "X" + Style.RESET_ALL, end="")
            T[i][j] = 'X'
        elif i == 1:
            print(Fore.RED + "X" + Style.RESET_ALL, end="")
            T[i][j] = 'X'
        elif i == 2:
            print(Fore.RED + "X" + Style.RESET_ALL, end="")
            T[i][j] = 'X'
        else:
            print("Linha inválida", end="")
    else:
            # jogada da IA (jogador 2)
        print("Jogada do computador (jogador O)")
        melhor_valor = -float('inf')
        melhor_jogada = None
        for i in range(3):
            for j in range(3):
                if T[i][j] == 0:
                    T[i][j] = 2
                    valor = minimax(T, 'X', 0)
                    T[i][j] = 0
                    if valor > melhor_valor:
                        melhor_valor = valor
                        melhor_jogada = (i, j)
        T[melhor_jogada[0]][melhor_jogada[1]] = 'O'
        
        
# jogando até que alguém ganhe ou não haja mais posições livres
jogador_atual = 'X'
while True:
    if jogar(jogador_atual):
        print("Jogador", jogador_atual, "venceu!")
        break
    imprimir_tabuleiro()  # exibir tabuleiro apos cada jogada
    jogador_atual = 'O' if jogador_atual == 'X' else 'X'
    # verificando se há posições livres no tabuleiro
    if all(all(row) for row in T):
        print("Não há mais posições livres!")
        break
    # imprimir_tabuleiro()  



jogar(jogador='X')