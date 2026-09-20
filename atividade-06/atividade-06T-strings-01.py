# https://neps.academy/br/exercise/1721

def main():
    quantidade = int(input())
    stringA = input()
    stringB = input()

    if 1 <= quantidade <= 200:
        pass
    else:
        return

    letrasA = []
    for letra in list(stringA):
        if letra.isalpha():
            letrasA.append(letra)

    letrasB = []
    for letra in list(stringB):
        if letra.isalpha():
            letrasB.append(letra)

    if sorted(letrasA) == sorted(letrasB):
        print("S")
    else:
        print("N")


if __name__ == "__main__":
    main()
