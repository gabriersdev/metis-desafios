def main():
    X = int(input())
    ehPrimo = True

    if 1 <= X <= 10 ** 5:
        if X < 2:
            ehPrimo = False

        # Verifica se é primo
        for divisor in range(2, int(X ** 0.5) + 1):
            if X % divisor == 0:
                ehPrimo = False
                break

        if ehPrimo:
            print("S")
        else:
            print("N")


if __name__ == "__main__":
    main()
