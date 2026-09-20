# https://neps.academy/br/exercise/202
import re


def main():
    matriz = [[0] * 3 for _ in range(3)]
    valores = []

    for x in range(len(matriz)):
        for i in range(len(matriz[x])):
            valor = int(input())
            valores.append(valor)
            matriz[x][i] = valor

    maiorValor = max(valores)

    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            if matriz[x][y] == maiorValor:
                matriz[x][y] = -1

    for x in range(len(matriz)):
        print(re.sub(pattern=r",\s", repl=" ", string=str(matriz[x])[1:-1]))


if __name__ == "__main__":
    main()
