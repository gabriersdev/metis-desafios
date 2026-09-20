# https://neps.academy/br/exercise/49

def main():
    N = int(input())
    sequencia = input().split()

    if 3 <= N <= (10 ** 4):
        fita = [int(x) for x in sequencia]

        # Passagem da esquerda para a direita
        dist = float('inf')
        for i in range(N):
            if fita[i] == 0:
                dist = 0
            else:
                dist += 1
                fita[i] = dist

        # Passagem da direita para a esquerda
        dist = float('inf')
        for i in range(N - 1, -1, -1):
            if fita[i] == 0:
                dist = 0
            else:
                dist += 1
                fita[i] = min(fita[i], dist)

        # Limitar as cores ao tom máximo 9
        for i in range(N):
            if fita[i] > 9:
                fita[i] = 9

        print(" ".join(map(str, fita)))


if __name__ == "__main__":
    main()
