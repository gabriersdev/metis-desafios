# https://neps.academy/br/exercise/1726

def main():
    quantidadeLetras = int(input())
    string = input().strip()

    for tamanhoRaiz in range(1, (quantidadeLetras // 2) + 1):
        if quantidadeLetras % tamanhoRaiz == 0:
            raiz = string[:tamanhoRaiz]

            raizOrdenada = sorted(raiz)
            ehPoligrama = True

            for i in range(tamanhoRaiz, quantidadeLetras, tamanhoRaiz):
                pedaco = string[i: i + tamanhoRaiz]

                if sorted(pedaco) != raizOrdenada:
                    ehPoligrama = False
                    break

            if ehPoligrama:
                print(raiz)
                return

    print("*")


if __name__ == '__main__':
    main()
