# https://neps.academy/br/exercise/329

def main():
    M, N = map(int, input().split())

    matriz = [["" for _ in range(N)] for _ in range(M)]

    for i in range(M):
        linha = input()
        for j in range(N):
            matriz[i][j] = linha[j]

    costa = 0

    for i in range(M):
        for j in range(N):
            if matriz[i][j] == '#':
                isCosta = False

                # Cima
                if i == 0 or matriz[i - 1][j] == '.':
                    isCosta = True

                # Baixo
                elif i == M - 1 or matriz[i + 1][j] == '.':
                    isCosta = True

                # Esquerda
                elif j == 0 or matriz[i][j - 1] == '.':
                    isCosta = True

                # Direita
                elif j == N - 1 or matriz[i][j + 1] == '.':
                    isCosta = True

                if isCosta:
                    costa += 1

    print(costa)


if __name__ == "__main__":
    main()
