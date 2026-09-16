def main():
    # Nesse script não precisa da variável N, contudo ela é necessária para ser aceito pela plataforma
    comprimentoN = int(input())
    stringS = input()

    contadorVogais = 0
    vogais = ["a", "e", "i", "o", "u"]

    if 1 <= comprimentoN <= 50:
        for string in list(stringS):
            if string.lower() in vogais:
                contadorVogais += 1

        print(contadorVogais)


if __name__ == "__main__":
    main()
