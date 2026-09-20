# https://neps.academy/br/exercise/52

def main():
    quantidadeApertos = int(input())
    serieInteracoes = input()

    lampadaAAcesa, lampadaBAcesa = False, False

    if 2 <= quantidadeApertos <= (10 ** 5):
        for string in serieInteracoes.split(" "):
            if string == "1":
                lampadaAAcesa = not lampadaAAcesa
            elif string == "2":
                lampadaBAcesa = not lampadaBAcesa
                lampadaAAcesa = not lampadaAAcesa

        print(1 if lampadaAAcesa else 0)
        print(1 if lampadaBAcesa else 0)


if __name__ == "__main__":
    main()
