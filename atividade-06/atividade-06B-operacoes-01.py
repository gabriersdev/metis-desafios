def main():
    M = int(input())
    A = int(input())
    B = int(input())

    if (40 <= M <= 110) and (1 <= A <= M) and (1 <= B <= M) and (A != B):
        C = M - A - B
        # Descobre a idade do mais velho
        idades = [A, B, C]
        maisVelho = 0

        for idade in idades:
            if idade > maisVelho:
                maisVelho = idade

        print(maisVelho)


if __name__ == '__main__':
    main()
