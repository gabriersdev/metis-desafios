# https://neps.academy/br/exercise/2793

def main():
    quantidadeLinhas = int(input())

    if 1 <= quantidadeLinhas <= 100000:
        posicoes = [0] * (quantidadeLinhas + 1)

        for posicao in range(1, quantidadeLinhas + 1):
            atleta = int(input())
            posicoes[atleta] = posicao

        for atleta in range(1, quantidadeLinhas + 1):
            print(posicoes[atleta])


if __name__ == "__main__":
    main()
