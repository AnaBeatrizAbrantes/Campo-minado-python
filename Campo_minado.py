import random
import time

def criar_tabuleiro(linhas, colunas, qtd_minas):
    tabuleiro = [[" " for _ in range(colunas)] for _ in range(linhas)]
    minas = 0

    while minas < qtd_minas:
        x = random.randint(0, colunas - 1)
        y = random.randint(0, linhas - 1)
        if tabuleiro[y][x] != "*":
            tabuleiro[y][x] = "*"
            minas += 1
    return tabuleiro

def mostrar_tabuleiro(tabuleiro, revelado):
    print("   " + "  ".join([str(i + 1) for i in range(len(tabuleiro[0]))]))
    print("  " + "=====" * len(tabuleiro[0]))
    for i in range(len(tabuleiro)):
        print(f"{i + 1}|", end=" ")
        for j in range(len(tabuleiro[i])):
            if revelado[i][j]:
                print(tabuleiro[i][j], end="  ")
            else:
                print("■", end="  ")
        print()
    print()

def contar_minas(tabuleiro, linha, coluna):
    minas = 0
    for i in range(linha - 1, linha + 2):
        for j in range(coluna - 1, coluna + 2):
            if 0 <= i < len(tabuleiro) and 0 <= j < len(tabuleiro[0]):
                if tabuleiro[i][j] == "*":
                    minas += 1
    return minas

def jogar():
    linhas = 5
    colunas = 5
    qtd_minas = 5
    tabuleiro = criar_tabuleiro(linhas, colunas, qtd_minas)
    revelado = [[False for _ in range(colunas)] for _ in range(linhas)]

    print("===================================")
    print("           CAMPO MINADO ")
    print("===================================")
    print("Abra todos espaços seguros e evite as minas!\n")
    time.sleep(1)

    while True:
        mostrar_tabuleiro(tabuleiro, revelado)

        try:
            linha = int(input("Linha (1-5): ")) - 1
            coluna = int(input("Coluna (1-5): ")) - 1

            if linha not in range(linhas) or coluna not in range(colunas):
                print("Coordenadas inválidas! Tente novamente.\n")
                continue

            if tabuleiro[linha][coluna] == "*":
                print("\n BOOM! Você pisou em uma mina!\n")
                for i in range(linhas):
                    for j in range(colunas):
                        revelado[i][j] = True
                mostrar_tabuleiro(tabuleiro, revelado)
                print("===== FIM DE JOGO =====")
                break

            minas_vizinhas = contar_minas(tabuleiro, linha, coluna)
            tabuleiro[linha][coluna] = str(minas_vizinhas)
            revelado[linha][coluna] = True

            abertas = sum(1 for i in range(linhas) for j in range(colunas) if revelado[i][j])
            if abertas == (linhas * colunas) - qtd_minas:
                mostrar_tabuleiro(tabuleiro, revelado)
                print(" PARABÉNS! Você venceu!\n")
                break

        except ValueError:
            print("Digite apenas números inteiros!\n")

if __name__ == "__main__":
    jogar()